from rtde_control import RTDEControlInterface as RTDEControl
from rtde_io import RTDEIOInterface
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import time
import threading
from compas.geometry import Frame, Transformation, Translation, Vector, Point
from compas.robots import Configuration

def get_config(ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    robot_joints = ur_r.getActualQ()
    config = Configuration.from_revolute_values(robot_joints)
    return config

def get_tcp_offset(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    tcp = ur_c.getTCPOffset()
    return tcp

def set_tcp_offset(pose, ip = "127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.setTcp(pose)

def move_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveJ(config.joint_values, speed, accel, nowait)

def movel_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveL_FK(config.joint_values, speed, accel, nowait)

def move_to_target(frame, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    pose = frame.point.x/1000, frame.point.y/1000, frame.point.z/1000, *frame.axis_angle_vector
    ur_c = RTDEControl(ip)
    ur_c.moveL(pose ,speed, accel, nowait)
    return pose

def pick_and_place_async(pick_frames, place_frames, speed, accel, ip, vaccum_io, safe_dist = 100):
    thread = threading.Thread(target=pick_and_place, args=(pick_frames, place_frames, speed, accel, ip, vaccum_io, safe_dist))
    thread.start()

def pick_and_place(pick_frames, place_frames, speed, accel, ip, vaccum_io, safe_dist = 100):
#move to pick safety plane
    if isinstance(pick_frames,Frame):
        pick_frames = [pick_frames]*len(place_frames)

    for pick, place in zip(pick_frames, place_frames):
        move_to_target(pick.transformed(Translation.from_vector(Vector(0,0,safe_dist))), speed, accel, False, ip = ip)
        #move to pick plane
        move_to_target(pick, speed, accel, False, ip = ip)
        #turn IO on
        set_digital_io(vaccum_io,True,ip=ip)
        #sleep on position to give some time to pick up
        time.sleep(0.5)
        #move to pick safety plane
        move_to_target(pick.transformed(Translation.from_vector(Vector(0,0,safe_dist))), speed, accel, False, ip = ip)
        #move to pre placement frame
        pre_place_frame = place.transformed(Translation.from_vector(Vector(0,0,safe_dist)))
        move_to_target(pre_place_frame, speed, accel, False, ip = ip)
        #move to placement frame
        move_to_target(place, speed, accel, False, ip = ip)
        #turn vaccuum off to place brick
        set_digital_io(vaccum_io,False,ip=ip)
        #sleep robot to make sure it is placed
        time.sleep(0.5)
        #move to post placement frame
        post_place_frame = place.transformed(Translation.from_vector(Vector(0,0,safe_dist)))
        move_to_target(post_place_frame, speed, accel, False, ip = ip)

def create_path(frames, speed, accel, radius):
    # speed rad/s, accel rad/s^2, nowait bool
    path = []
    for f in frames:
        pose = f.point.x/1000, f.point.y/1000, f.point.z/1000, *f.axis_angle_vector
        target = [*pose,speed,accel, radius]
        path.append(target)
    return path

def move_to_path(frames, speed, accel, radius, ip = "127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    path = create_path(frames, speed, accel, radius)
    ur_c.moveL(path, True)
    return path

def stopL(accel, ip = "127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.stopL(accel)

def get_digital_io(signal, ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    return ur_r.getDigitalOutState(signal)

def set_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setStandardDigitalOut(signal, value)

def set_tool_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setToolDigitalOut(signal, value)

def get_tcp_frame(ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    tcp = ur_r.getActualTCPPose()
    frame = Frame.from_axis_angle_vector(tcp[3:], point=tcp[0:3])
    return frame

def move_trajectory(configurations, speed, accel, blend, ur_c):
    path = []
    for config in configurations:
        path.append(config.joint_values + [speed, accel, blend])
    if len(path):
        ur_c.moveJ(path)

def start_teach_mode(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.teachMode()

def stop_teach_mode(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.endTeachMode()



if __name__ == "__main__":
#    print(get_config("192.168.10.12"))

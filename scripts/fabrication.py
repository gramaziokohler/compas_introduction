from rtde_control import RTDEControlInterface as RTDEControl
from rtde_io import RTDEIOInterface
from rtde_receive import RTDEReceiveInterface as RTDEReceive

from compas.geometry import Frame
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


def move_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveJ(config.joint_values, speed, accel, nowait)


def movel_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveL_FK(config.joint_values, speed, accel, nowait)


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
    ip = "127.0.0.1"
    frame = get_tcp_frame(ip)
    print(frame)

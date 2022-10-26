from compas_fab.backends import RosClient

with RosClient("localhost") as client:
    robot = client.load_robot()

    configuration = robot.zero_configuration()
    configuration.joint_values = (-0.106, -5.254, -2.231, 5.915, 4.712, -4.818)

    frame_WCF = robot.forward_kinematics(configuration)

    print("Frame in the world coordinate system")
    print(frame_WCF)

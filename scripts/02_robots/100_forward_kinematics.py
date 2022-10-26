from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=False)

# Get some relevant link names for FK
base = model.get_base_link_name()
endeffector = model.get_end_effector_link_name()
print(base)
print(endeffector)

# Create config
config = model.zero_configuration()

# Get FK for tip
frame_tip = model.forward_kinematics(config)
print(frame_tip)

# Get FK for base
frame_base = model.forward_kinematics(config, link_name=base)
print(frame_base)

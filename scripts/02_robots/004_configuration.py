# Units: radians (revolute joints), meters (prismatic joints)
import math

from compas.robots import Configuration

print("Access and update of configuration")
config = Configuration.from_revolute_values([math.pi, 0], ["joint_1", "joint_2"])
print("Joint 1: {:.3f}, Joint 2: {:.3f}".format(config["joint_1"], config["joint_2"]))
config["joint_1"] = math.pi / 2
config["joint_2"] = math.pi
print(config)

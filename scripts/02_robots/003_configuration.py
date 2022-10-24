# Units: radians (revolute joints), meters (prismatic joints)
import math

from compas.robots import Configuration
from compas.robots import Joint

print("Merge two configurations")
config_a = Configuration([4], [Joint.PRISMATIC], ["ext_axis_1"])
config_b = Configuration([math.pi], [Joint.REVOLUTE], ["joint_1"])
config_c = config_a.merged(config_b)
print(config_c)

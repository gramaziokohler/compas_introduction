# Units: radians (revolute joints), meters (prismatic joints)
import math

from compas.robots import Configuration
from compas.robots import Joint

print("Default constructor (radians & meters!)")
config = Configuration([math.pi, 4], [Joint.REVOLUTE, Joint.PRISMATIC], ["joint_1", "ext_axis_1"])
print(config)

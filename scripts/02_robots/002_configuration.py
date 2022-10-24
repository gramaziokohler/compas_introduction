# Units: radians (revolute joints), meters (prismatic joints)
import math

from compas.robots import Configuration
from compas.robots import Joint

print("Construct from prismatic & revolute values")
config = Configuration.from_prismatic_and_revolute_values([4], [math.pi], ["ext_axis_1", "joint_1"])
print(config)

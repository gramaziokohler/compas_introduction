# Units: radians (revolute joints), meters (prismatic joints)
import math

from compas.robots import Configuration
from compas.robots import Joint

print("Construct from revolute values")
config = Configuration.from_revolute_values([math.pi, 0], ["joint_1", "joint_2"])
print(config)

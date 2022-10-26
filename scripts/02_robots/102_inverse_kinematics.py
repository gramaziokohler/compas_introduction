from compas_fab.backends import UR10eKinematics

from compas.geometry import Frame
from compas.robots import Configuration

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.00), (1.000, 0.000, 0.000))

solver = UR10eKinematics()
solutions = solver.inverse(f)

for jv in solutions:
    print(Configuration.from_revolute_values(jv))

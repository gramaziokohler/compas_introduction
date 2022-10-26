from collections import deque
from compas.artists import Artist


def show_trajectory(trajectory):
    import matplotlib.pyplot as plt

    # visualise
    positions = []
    velocities = []
    accelerations = []
    time_from_start = []

    for p in trajectory.points:
        positions.append(p.positions)
        velocities.append(p.velocities)
        accelerations.append(p.accelerations)
        time_from_start.append(p.time_from_start.seconds)

    plt.rcParams["figure.figsize"] = [17, 4]
    plt.subplot(131)
    plt.title("positions")
    plt.plot(positions)
    plt.subplot(132)
    plt.plot(velocities)
    plt.title("velocities")
    plt.subplot(133)
    plt.plot(accelerations)
    plt.title("accelerations")
    plt.show()


def traverse(assembly, k):
    tovisit = deque([k])
    visited = set([k])
    ordering = [k]
    while tovisit:
        node = tovisit.popleft()
        for nbr in assembly.graph.neighbors_in(node):
            if nbr not in visited:
                tovisit.append(nbr)
                visited.add(nbr)
                ordering.append(nbr)
    return ordering


def draw_parts(assembly):
    import compas_ghpython

    points = [{"pos": list(part.frame.point)} for part in assembly.parts()]
    return compas_ghpython.draw_points(points)


def draw_connections(assembly):
    import compas_ghpython

    lines = []

    for u, v in assembly.connections():
        u = assembly.find_by_key(u)
        v = assembly.find_by_key(v)
        lines.append(
            {
                "start": list(u.frame.point),
                "end": list(v.frame.point),
            }
        )
    return compas_ghpython.draw_lines(lines)


def draw_parts_attribute(assembly, attribute_name):
    return [Artist(p.attributes[attribute_name]).draw() for p in assembly.parts()]


def get_assembly_sequence(assembly, top_course):
    sequence = []
    sequence_set = set(sequence)

    course_parts = list(assembly.graph.nodes_where_predicate(lambda key, attr: attr["part"].attributes["course"] == top_course))

    for c in course_parts:
        parts = traverse(assembly, c)

        for part in reversed(parts):
            if part in sequence_set:
                continue
            sequence.append(part)
            sequence_set.add(part)
            part = assembly.find_by_key(part)

    return sequence

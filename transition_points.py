from points_python import dragon_points
from stable_matcher import StableMatcher, get_preferences_list
import math


def distance(point1, point2):
    return math.sqrt(
        sum(
            [
                (coordinate1 - coordinate2) ** 2
                for coordinate1, coordinate2 in zip(point1, point2)
            ]
        )
    )


def transition_desmos_str(start_point, end_point):
    return (
        "("
        + ",".join([f"{x1}(1 - t) + {x2}t" for x1, x2 in zip(start_point, end_point)])
        + ")"
    )


def transition_python_str(start_point, end_point):
    return (
        "("
        + ",".join(
            [
                f"lambda t: {x1} * (1 - t) + {x2} * t"
                for x1, x2 in zip(start_point, end_point)
            ]
        )
        + ")"
    )


if __name__ == "__main__":
    scale_factor = 8
    resolution = (4 * scale_factor, 3 * scale_factor)

    # -100 < x < 100
    # -100 < y < 90
    #  -10 < z < 130

    # screen
    # x: -100 to 100 (spread 4 * scale_factor of them)
    # y: 0
    # z: 130 (spread 3 * scale_factor)

    x_factor = 200 / resolution[0]
    x_offset = -100

    z_factor = 130 / resolution[1]

    # (x, y, z)

    start = dragon_points

    end = [
        (int(x_factor * i + x_offset), 0, int(z_factor * j))
        for i in range(resolution[0])
        for j in range(resolution[1])
    ] + [
        (4 * i // 20 - 40, 4 * (i % 20) - 40, -100)
        for i in range(len(dragon_points) - resolution[0] * resolution[1])
    ]

    print("len(start):", len(start))
    print("len(end):", len(end))

    print("len(dragon_points) - resoultion[0] * resolution[1]:", len(dragon_points) - resolution[0] * resolution[1])

    # print(",".join([f"({x}, {y}, {z})" for x, y, z in end]))

    start_preferences = get_preferences_list(start, end, distance)

    end_preferences = get_preferences_list(end, start, distance)

    matcher = StableMatcher(start_preferences, end_preferences)

    matchings = matcher.match()

    transition_desmos = []
    transition_python = []

    for start_index, end_index in matchings:
        transition_desmos.append(
            transition_desmos_str(start[start_index], end[end_index])
        )
        transition_python.append(
            transition_python_str(start[start_index], end[end_index])
        )

    with open("/Users/harqian/projects/drone_modeling/transition_desmos.txt", "w") as f:
        f.write(",".join(transition_desmos))

    with open("/Users/harqian/projects/drone_modeling/transition_python.py", "w") as f:
        f.write("transition_points = [" + ",".join(transition_python) + "]")

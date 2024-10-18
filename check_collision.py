from transition_python import transition_points

def check_collisions(transition_points, t, distance_threshold):
    for i in range(len(transition_points)):
        for j in range(len(transition_points)):
            if j < i:
                x1, y1, z1 = transition_points[i]
                x2, y2, z2 = transition_points[j]
                distance = ((x1(t) - x2(t)) ** 2 + (y1(t) - y2(t)) ** 2 + (z1(t) - z2(t)) ** 2) ** (1/2)
                if distance < distance_threshold:
                    print(((x1(t), y1(t), z1(t)), (x2(t), y2(t), z2(t)), distance, t))

interval = 1
time_steps = list(range(0, 100 + interval, interval))

distance_threshold = 1

for t in time_steps:
    t = t / 100
    check_collisions(transition_points, t, distance_threshold)

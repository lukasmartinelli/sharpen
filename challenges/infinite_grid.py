

def steps(points):
    moves = 0
    for prev_point, point in zip(points, points[1:]):
        prev_x, prev_y = prev_point
        x, y = point

        x_dist = abs(x - prev_x)
        y_dist = abs(y - prev_y)
        moves += max(x_dist, y_dist)

    return moves


print(steps([(0,0), (-2, 2)]))
print(steps([(0,0), (-4, 2), (0, -2)]))

print(steps([(0,0), (1, 1), (5, 2)]))

import math


def grid_unique_paths(m, n):
    if m < 2 or n < 2:
        return 1

    max_path_length = m + n - 2
    down_steps = m - 1
    right_steps = n - 1
    return math.factorial(max_path_length) / (math.factorial(down_steps)*math.factorial(right_steps))


def grid_unique_paths_slow(m, n):
    if m < 2 or n < 2:
        return 1

    max_path_length = m + n - 2

    def generate_path(path_length, path_sum):
        if path_sum > n - 1:
            return 0

        if path_length >= max_path_length:
            if path_sum == n - 1:
                return 1
            else:
                return 0

        p1 = generate_path(path_length + 1, path_sum + 0)
        p2 = generate_path(path_length + 1, path_sum + 1)
        return p1 + p2

    return generate_path(0, 0)

assert grid_unique_paths(3, 5) == 15
assert grid_unique_paths(2, 2) == 2
assert grid_unique_paths(3, 3) == 6
assert grid_unique_paths(4, 4) == 20
assert grid_unique_paths(5, 4) == 35
assert grid_unique_paths(0, 0) == 1
assert grid_unique_paths(1, 1) == 1
assert grid_unique_paths(1, 2) == 1
assert grid_unique_paths(5, 5) == 70
assert grid_unique_paths(15, 12) == 4457400

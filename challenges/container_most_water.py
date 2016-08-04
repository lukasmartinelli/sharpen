def container_most_water(heights):
    coords = zip(range(0, len(heights)), heights)
    i = 0
    j = len(coords) - 1

    max_area = 0
    while i != j:
        height = min(heights[i], heights[j])
        width = abs(j - i)
        area = height * width
        print('({}, {}) <=> ({}, {}) => {}'.format(i, heights[i], j, heights[j], area))

        if heights[i] <= heights[j]:
            i += 1
        elif heights[i] > heights[j]:
            j -= 1

        max_area = max(max_area, area)

    return max_area


def test_container_most_water():
    assert container_most_water([3, 4, 8, 10, 3, 6, 8, 3, 4, 1]) == 32
    assert container_most_water([1, 5, 4, 3]) == 6

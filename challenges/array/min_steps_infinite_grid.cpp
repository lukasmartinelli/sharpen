
#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <unordered_map>

typedef std::tuple<int, int> t_point;

int dist(t_point p1, t_point p2) {
    const auto prev_x = std::get<0>(p1);
    const auto prev_y = std::get<1>(p1);

    const auto cur_x = std::get<0>(p2);
    const auto cur_y = std::get<1>(p2);

    const auto dist_x = std::abs(cur_x - prev_x);
    const auto dist_y = std::abs(cur_y - prev_y);

    return std::max(dist_x, dist_y);
}

int cover_points(const std::vector<t_point> points) {
    int min_steps {0};

    for (auto it=points.begin(); it!=points.end(); ++it) {
        if(it == points.begin()) continue;

        min_steps += dist(*std::prev(it, 1), *it);
    }
    return min_steps;
}

int main() {
    std::vector<t_point> e1 = {
         std::make_tuple(0, 0),
         std::make_tuple(-2, 2)
    };
    assert(cover_points(e1) == 2);

    std::vector<t_point> e2 = {
         std::make_tuple(0, 0),
         std::make_tuple(-4, 2),
         std::make_tuple(0, -2)
    };
    assert(cover_points(e2) == 8);

    std::vector<t_point> e3 = {
         std::make_tuple(0, 0),
         std::make_tuple(1, 1),
         std::make_tuple(5, 2)
    };
    assert(cover_points(e3) == 5);
}

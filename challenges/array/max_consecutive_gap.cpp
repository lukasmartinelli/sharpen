#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <unordered_map>

int max_gap(std::vector<int> elements) {
    std::sort(elements.begin(), elements.end());
    int max {0};
    for (auto it=elements.begin(); it!=elements.end(); ++it) {
        auto prev_it = std::prev(it);
        if (prev_it == elements.begin()) continue;
        const int prev_elem = *prev_it;
        const int cur_elem = *it;
        max = std::max(max, cur_elem - prev_elem);
    }
    return max;
}

int main() {
    std::vector<int> e1 = {1, 10, 5};
    assert(max_gap(e1) == 5);
}

#include <vector>
#include <cassert>
#include <iostream>
#include <unordered_map>

typedef std::vector<int>::size_type idx_t;

int count_adjacent_same(std::vector<int> elements, idx_t start_idx) {
    int count {0};

    for(auto i = start_idx; i != 0; i--) {
        if(elements[i] == elements[start_idx]) {
            count += 1;
        } else {
            break;
        }
    }

    for(auto i = start_idx+1; i < elements.size(); i++) {
        if(elements[i] == elements[start_idx]) {
            count += 1;
        } else {
            break;
        }
    }
    return count;
}

int count_element(std::vector<int> elements, int element) {
    idx_t lower_idx {0};
    idx_t upper_idx {elements.size()};

    while(upper_idx > lower_idx) {
        auto mid_idx = (upper_idx+lower_idx)/2;
        auto mid = elements[mid_idx];
        if (mid == element) {
            return count_adjacent_same(elements, mid_idx);
        } else if (mid < element) {
            lower_idx = mid_idx;
        } else if (mid > element) {
            upper_idx = mid_idx;
        }
    }
    return -1;
}

int main() {
    std::vector<int> e1 = {1, 1, 2, 3, 4, 5, 6};
    assert(count_element(e1, 3) == 1);

    std::vector<int> e2 = {1, 1, 2, 2, 4, 5, 5, 5, 6};
    assert(count_element(e2, 5) == 3);
}

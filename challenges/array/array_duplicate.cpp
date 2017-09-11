#include <vector>
#include <cassert>
#include <iostream>
#include <unordered_map>

int find_duplicate(std::vector<uint32_t> elements) {
    std::unordered_map<uint32_t, bool> lookup{};

    for (auto it=elements.begin(); it!=elements.end(); ++it) {
        if (lookup.find(*it) != lookup.end()) {
            return *it;
        } else {
            lookup[*it] = true;
        }
    }
    return -1;
}

int main() {
    std::vector<uint32_t> e1 = {3, 4, 1, 4, 5};
    assert(find_duplicate(e1) == 4);

    std::vector<uint32_t> e2 = {1, 2, 3, 4, 5, 1};
    assert(find_duplicate(e2) == 1);

    std::vector<uint32_t> e3 = {1, 2, 3};
    assert(find_duplicate(e3) == -1);
}

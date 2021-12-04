#include "compute.hpp"

int input_data[INPUT_DATA_SIZE];

int main() {
    printf("Loading data...\n");
    std::fstream fs;
    fs.open("./input.txt");
    int k;
    int idx = 0;
    while (fs >> k) {
        input_data[idx] = (int)k;
        idx++;
    }

    int part_1;
    part_1 = compute_part_1(input_data);
    printf("Part 1: %i\n", part_1);

    return 0;
}
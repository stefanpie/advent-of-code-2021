#include "compute.hpp"

void compute_part_1(int input_data[INPUT_DATA_SIZE], int output) {
    int count = 0;
    for (int i = 1; i < INPUT_DATA_SIZE; i++) {
        int diff = input_data[i] - input_data[i-1];
        if (diff>0)
        {
            count+=1;
        }
    }
    output = count;
}
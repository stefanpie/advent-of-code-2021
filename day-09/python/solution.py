from pathlib import Path
import numpy as np
from scipy.signal import argrelextrema


current_script_dir = Path(__file__).parent


def check_if_idx_in_shape(idx: tuple, shape: tuple) -> bool:
        return all([i >= 0 and i < shape[j] for j, i in enumerate(idx)])

def find_local_minimums(data: np.ndarray) -> np.ndarray:
    data_shape = data.shape
    local_min = np.zeros_like(data, dtype=bool)

    for i in range(0, data.shape[0] ):
        for j in range(0, data.shape[1]):
            top_idx = (i - 1, j)
            bottom_idx = (i + 1, j)
            left_idx = (i, j - 1)
            right_idx = (i, j + 1)
            top_idx_check = check_if_idx_in_shape(top_idx, data_shape)
            bottom_idx_check = check_if_idx_in_shape(bottom_idx, data_shape)
            left_idx_check = check_if_idx_in_shape(left_idx, data_shape)
            right_idx_check = check_if_idx_in_shape(right_idx, data_shape)

            is_min = True
            if top_idx_check:
                is_min &= data[i, j] < data[top_idx]
            if bottom_idx_check:
                is_min &= data[i, j] < data[bottom_idx]
            if left_idx_check:
                is_min &= data[i, j] < data[left_idx]
            if right_idx_check:
                is_min &= data[i, j] < data[right_idx]

            local_min[i, j] = is_min

    return local_min

# Next, you need to find the largest basins so you know what areas are most important to avoid.
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
def find_basins(data):
    local_mins = find_local_minimums(data)

    basins = np.zeros_like(data, dtype=int)
    

if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    with open(current_script_dir / "input.txt") as f:
        input_data = f.read().splitlines()
    input_data_array = [list(map(int, list(line))) for line in input_data]
    data = np.asarray(input_data_array)
    
    local_mins = find_local_minimums(data)
    local_mins_int = local_mins.astype(int)
    local_mins_gathered = data[local_mins_int == 1]
    sum_risk_levels = np.sum(local_mins_gathered+1)

    part_1 = sum_risk_levels
    print(f"Part 1: {part_1}")

    part_2 = None
    print(f"Part 2: {part_2}")

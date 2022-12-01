from collections import defaultdict, OrderedDict
from pprint import pprint as pp
import math
import uuid
import copy


def calculate_growth(state, days):
    state = state
    state_next = defaultdict(lambda: 0)

    for d in range(days):

        for i in range(8+1):
            if i == 0:
                state_next[6] += state[i]
                state_next[8] += state[i]
            else:
                state_next[i-1] += state[i]

        state = copy.copy(state_next)
        state_next = defaultdict(lambda: 0)

    total_fish = sum(state.values())

    return total_fish


if __name__ == "__main__":

    with open("./input.txt") as f:
        input_data = f.read().strip()

    input_data = list(map(int, input_data.split(",")))

    initial_state = {}
    for i in range(8+1):
        initial_state[i] = input_data.count(i)

    fish_count_80 = calculate_growth(initial_state, 80)
    part_1 = fish_count_80
    print(f"Part 1: {part_1}")

    fish_count_256 = calculate_growth(initial_state, 256)
    part_2 = fish_count_256
    print(f"Part 2: {part_2}")

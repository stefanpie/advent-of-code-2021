from pprint import pprint as pp
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

import pulp


SEGMENTS = ["a", "b", "c", "d", "e", "f"]
DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

COUNT_LOOKUP = {2: {1},
                4: {4},
                3: {7},
                7: {8},
                5: {2, 3, 5},
                6: {0, 6, 9}}

COUNT_LOOKUP_REVERSE = {}
for k, value in COUNT_LOOKUP.items():
    for v in value:
        COUNT_LOOKUP_REVERSE[v] = k


def decode_entry(entry):
    digits_count = [len(d) for d in entry["digits"]]
    for i, d_c in enumerate(digits_count):
        # unique digits
        if d_c == 2:  # digit one
            entry["digits_solved"][i] = 1
            entry["digit_mapping"][1] |= entry["digits"][i]
        if d_c == 4:  # digit 4
            entry["digits_solved"][i] = 4
            entry["digit_mapping"][4] |= entry["digits"][i]
        if d_c == 3:  # digit 7
            entry["digits_solved"][i] = 7
            entry["digit_mapping"][7] |= entry["digits"][i]
        if d_c == 7:  # digit 8
            entry["digits_solved"][i] = 8
            entry["digit_mapping"][8] |= entry["digits"][i]

        # # ambigious digits
        # if d_c == 5:  # digit 2, 3, 5
        #    entry["digit_mapping"][2] |= entry["digits"][i]
        #    entry["digit_mapping"][3] |= entry["digits"][i]
        #    entry["digit_mapping"][5] |= entry["digits"][i]
        # if d_c == 6:  # digit 0, 6, 9
        #    entry["digit_mapping"][0] |= entry["digits"][i]
        #    entry["digit_mapping"][6] |= entry["digits"][i]
        #    entry["digit_mapping"][9] |= entry["digits"][i]

    # pp(entry["digit_mapping"])

    prob = pulp.LpProblem("segment_assignment")
    assignments = pulp.LpVariable.dicts("assignments", (DIGITS, SEGMENTS), cat="Binary")

    for d in DIGITS:
        # prob += pulp.lpSum(assignments[d]) == COUNT_LOOKUP_REVERSE[d]-1
        # prob += pulp.lpSum(assignments[d]) >= 1 

        if len(entry["digit_mapping"][d]) != 0:
            for s in SEGMENTS:
                prob += assignments[d][s] == bool(s in entry["digit_mapping"][d])
    
    print(prob)
    prob.solve()
    print("Status:", pulp.LpStatus[prob.status])
    pp(prob.variables())
    for v in prob.variables():
        print(v.name, "=", v.varValue)


    # for c in entry["combos"]:
    #     possible_digits = COUNT_LOOKUP[len(c)]
    #     for d in possible_digits:
            
    #     pulp.

    input("...")
    print()
    return entry


if __name__ == "__main__":

    with open("./input_small_2.txt") as f:
        input_data = f.readlines()

    input_data = [l.strip() for l in input_data]
    input_data = [l.split(" | ") for l in input_data]
    input_data = [list(map(str.split, l)) for l in input_data]

    def process_input_data_entry(entry):
        data = {}
        data["combos"] = list(map(set, map(list, entry[0])))
        data["digits"] = list(map(set, map(list, entry[1])))
        data["digits_solved"] = [None for _ in range(4)]
        data["digit_mapping"] = {d: set() for d in DIGITS}
        data["digit_mapping_array"] = np.zeros((len(DIGITS), len(SEGMENTS)))
        return data

    data = list(map(process_input_data_entry, input_data))
    data = list(map(decode_entry, data))
    # pp(data)

    count = sum([len([x for x in entry["digits_solved"] if x is not None]) for entry in data])

    part_1 = count
    print(f"Part 1: {part_1}")

    part_2 = None
    print(f"Part 2: {part_2}")

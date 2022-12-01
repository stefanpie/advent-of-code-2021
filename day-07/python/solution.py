from pprint import pprint as pp
import statistics


def fuel_obj_1(middle, crab_x_positions):
    distances = [abs(middle-x) for x in crab_x_positions]
    return round(sum(distances))


def fuel_obj_2(middle, crab_x_positions):
    distances = [abs(middle-x) for x in crab_x_positions]
    fuels = [d*(d + 1)/2 for d in distances]
    return round(sum(fuels))


def fuel_optimization(crab_x_positions, part="part_1"):
    if part == "part_1":
        return round(statistics.median(crab_x_positions))
    if part == "part_2":
        return round(statistics.mean(crab_x_positions))


if __name__ == "__main__":

    with open("./input.txt") as f:
        input_data = f.read().strip()

    input_data = list(map(int, input_data.split(",")))
    input_data = input_data

    best_loc = fuel_optimization(input_data, part="part_1")
    best_loc_fuel = fuel_obj_1(best_loc, input_data)
    part_1 = best_loc_fuel
    print(f"Part 1: {part_1}")

    best_loc_2 = fuel_optimization(input_data, part="part_2")
    best_loc_fuel_2 = fuel_obj_2(best_loc_2, input_data)
    part_2 = best_loc_fuel_2
    print(f"Part 2: {part_2}")

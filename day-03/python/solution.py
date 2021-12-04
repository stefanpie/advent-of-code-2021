import numpy as np


def get_power_rates(report):
    rows = report.shape[0]
    sums = np.sum(report, axis=0)

    mode = sums > (rows//2)
    mode = mode.astype(int)

    gamma_binary = mode
    epsilon_binary = 1-mode

    gamma_rate = int("".join(map(str, gamma_binary.tolist())), 2)
    epsilon_rate = int("".join(map(str, epsilon_binary.tolist())), 2)

    return gamma_rate, epsilon_rate


def get_life_support_rates(report):
    oxygen_rating = report
    co2_rating = report

    for col in range(report.shape[1]):
        oxygen_counts = np.bincount(oxygen_rating[:, col])
        co2_counts = np.bincount(co2_rating[:, col])

        if oxygen_counts[0] == oxygen_counts[1]:
            oxygen_bit_criteria = 1
        else:
            oxygen_bit_criteria = np.argmax(oxygen_counts)

        oxygen_rating = oxygen_rating[oxygen_rating[:, col] == oxygen_bit_criteria]
        if oxygen_rating.shape[0] == 1:
            break

    for col in range(report.shape[1]):
        co2_counts = np.bincount(co2_rating[:, col])

        if co2_counts[0] == co2_counts[1]:
            co2_bit_criteria = 0
        else:
            co2_bit_criteria = np.argmin(co2_counts)
        
        co2_rating = co2_rating[co2_rating[:, col] == co2_bit_criteria]
        if co2_rating.shape[0] == 1:
            break
    
    oxygen_rating = oxygen_rating[0]
    co2_rating = co2_rating[0]

    oxygen_rating = int("".join(map(str, oxygen_rating.tolist())), 2)
    co2_rating = int("".join(map(str, co2_rating.tolist())), 2)

    return oxygen_rating, co2_rating


if __name__ == "__main__":

    with open("./input.txt") as f:
        input = f.readlines()

    input = [list(map(int, list(line.strip()))) for line in input]
    report = np.array(input)

    gamma_rate, epsilon_rate = get_power_rates(report)
    power_consumption = gamma_rate * epsilon_rate

    part_1 = power_consumption
    print(f"Part 1: {part_1}")

    oxygen_rating, co2_rating = get_life_support_rates(report)
    life_support_rating = oxygen_rating*co2_rating

    part_2 = life_support_rating
    print(f"Part 2: {part_2}")

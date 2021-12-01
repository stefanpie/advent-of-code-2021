if __name__ == "__main__":
    with open("./input.txt") as f:
        input_data = f.read().splitlines()
        input_data = [int(i) for i in input_data]
    
    delta_list = [input_data[n]-input_data[n-1] for n in range(1, len(input_data))]
    increasing_count = sum([x>0 for x in delta_list])

    part_1 = increasing_count
    print(f"Part 1: {part_1}")

    moving_sum = [input_data[n]+input_data[n-1]+input_data[n-2] for n in range(2, len(input_data))]
    delta_list_2 = [moving_sum[n]-moving_sum[n-1] for n in range(1, len(moving_sum))]
    increasing_count_2 = sum([x > 0 for x in delta_list_2])
    
    part_2 = increasing_count_2
    print(f"Part 2: {part_2}")

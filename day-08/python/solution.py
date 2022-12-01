from pprint import pp
from pathlib import Path



def decode_entry(entry):

    pattern_to_number_map = {
        pattern: None for pattern in entry["test_digits"]
    }

    def get_dict_inverse(dict_in):
        return {v: k for k, v in dict_in.items()}

    for pattern in pattern_to_number_map:
        if len(pattern) == 2:
            pattern_to_number_map[pattern] = 1
        elif len(pattern) == 4:
            pattern_to_number_map[pattern] = 4
        elif len(pattern) == 3:
            pattern_to_number_map[pattern] = 7
        elif len(pattern) == 7:
            pattern_to_number_map[pattern] = 8
        else:
            continue

    pattern_1 = get_dict_inverse(pattern_to_number_map)[1]
    pattern_4 = get_dict_inverse(pattern_to_number_map)[4]

    for pattern in pattern_to_number_map:
        if pattern_to_number_map[pattern] is not None:
            continue
        if len(pattern) == 5:
            if len(set(pattern).intersection(set(pattern_1))) == 2:
                pattern_to_number_map[pattern] = 3
            elif len(set(pattern).intersection(set(pattern_4))) == 3:
                pattern_to_number_map[pattern] = 5
            else:
                pattern_to_number_map[pattern] = 2
        elif len(pattern) == 6:
            if len(set(pattern).intersection(set(pattern_4))) == 4:
                pattern_to_number_map[pattern] = 9
            elif len(set(pattern).intersection(set(pattern_1))) == 2:
                pattern_to_number_map[pattern] = 0
            else:
                pattern_to_number_map[pattern] = 6
    

    decoded_output_digits = []
    for output_digit in entry["output_digits"]:
        decoded_output_digits.append(
            pattern_to_number_map[output_digit]
        )

    return decoded_output_digits

if __name__ == "__main__":
    current_script_dir = Path(__file__).parent
    with open(current_script_dir / "input.txt") as f:
        input_data = f.readlines()
    input_data = [line.strip() for line in input_data]

    entries = []
    for line in input_data:
        test_digits_str, output_digits_str = line.split(" | ")
        
        test_digits = test_digits_str.split(" ")
        test_digits = [''.join(sorted(digit)) for digit in test_digits]
        
        output_digits = output_digits_str.split(" ")
        output_digits = [''.join(sorted(digit)) for digit in output_digits]
        
        entry = {
            "test_digits": test_digits,
            "output_digits": output_digits
        }
        entries.append(entry)
    
    decoded_entries = [decode_entry(entry) for entry in entries]

    easy_numbers = [1,4,7,8]
    decoded_entries_flat = [digit for entry in decoded_entries for digit in entry]
    count_easy_numbers = sum([1 for digit in decoded_entries_flat if digit in easy_numbers])

    part_1 = count_easy_numbers
    print(f"Part 1: {part_1}")


    decoded_entries_int = [int(''.join([str(digit) for digit in entry])) for entry in decoded_entries]
    entries_sum = sum(decoded_entries_int)

    part_2 = entries_sum
    print(f"Part 2: {part_2}")

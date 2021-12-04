if __name__ == "__main__":
    with open("./input.txt") as f:
        input_data = f.read().splitlines()

    commands = [[c.split(" ")[0], int(c.split(" ")[1])] for c in input_data]
    print(commands)

    x = 0
    y = 0
    for c in commands:
        if c[0] == "up":
            y += c[1]
        if c[0] == "down":
            y -= c[1]
        if c[0] == "forward":
            x += c[1]

    part_1 = x * abs(y)
    print(f"Part 1: {part_1}")

    aim = 0
    x = 0
    y = 0
    for c in commands:
        if c[0] == "down":
            aim += c[1]
        if c[0] == "up":
            aim -= c[1]
        if c[0] == "forward":
            x += c[1]
            y -= c[1]*aim

    part_2 = x * abs(y)
    print(f"Part 2: {part_2}")

from collections import defaultdict
from pprint import pprint as pp
from typing import OrderedDict
import math


class Line:
    def __init__(self, id, input) -> None:
        self.id = id

        start, end = input.split(" -> ")
        self.start = list(map(int, start.split(",")))
        self.end = list(map(int, end.split(",")))

    def __repr__(self) -> str:
        return f"{self.id}: {self.start} -> {self.end}"

    def points(self, include_diagonals=False):
        points = []
        if (self.start[0] == self.end[0]) and not (self.start[1] == self.end[1]):
            start = min(self.start[1], self.end[1])
            end = max(self.start[1], self.end[1])
            for i in range(start, end+1):
                points.append([self.start[0], i])
        if (self.start[1] == self.end[1]) and not (self.start[0] == self.end[0]):
            start = min(self.start[0], self.end[0])
            end = max(self.start[0], self.end[0])
            for i in range(start, end+1):
                points.append([i, self.start[1]])
        if include_diagonals:
            if abs(self.end[0] - self.start[0]) == abs(self.start[1] - self.end[1]):
                x_dir = int(math.copysign(1, self.end[0] - self.start[0]))
                y_dir = int(math.copysign(1, self.end[1] - self.start[1]))
                for x, y in zip(range(self.start[0], self.end[0]+x_dir, x_dir), range(self.start[1], self.end[1]+y_dir, y_dir)):
                    points.append([x, y])

        return points


def print_ocean_map(ocean_map):
    min_x=min([k[0] for k in ocean_map])
    max_x=max([k[0] for k in ocean_map])
    min_y=min([k[1] for k in ocean_map])
    max_y=max([k[1] for k in ocean_map])

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (y, x) in ocean_map:
                print(len(ocean_map[(y, x)]), end = '')
            else:
                print(".", end = '')
        print("\n", end = '')

if __name__ == "__main__":

    with open("./input.txt") as f:
        input=f.readlines()

    lines=[line.strip() for line in input]
    lines=[Line(i, l) for i, l in enumerate(lines)]

    ocean_map=defaultdict(list)
    for l in lines:
        for p in l.points(include_diagonals=False):
            ocean_map[tuple(p)].append(l.id)
    danger_count=sum([len(ocean_map[k]) >= 2 for k in ocean_map])

    part_1=danger_count
    print(f"Part 1: {part_1}")

    ocean_map_2 = defaultdict(list)
    for l in lines:
        for p in l.points(include_diagonals=True):
            ocean_map_2[tuple(p)].append(l.id)
    danger_count_2 = sum([len(ocean_map_2[k]) >= 2 for k in ocean_map_2])

    part_2 = danger_count_2
    print(f"Part 2: {part_2}")

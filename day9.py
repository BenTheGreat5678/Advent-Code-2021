import numpy as np

with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums]
height_map = []
for num in num_list:
    dig_list = []
    for dig in num:
        dig_list.append(int(dig))
    height_map.append(dig_list)

low_points = []

for i, row in enumerate(height_map):
    for n, num in enumerate(row):
        if n > 0 and n < len(row) - 1 and i > 0 and i < len(height_map) - 1:
            if (
                num < row[n - 1]
                and num < row[n + 1]
                and num < height_map[i - 1][n]
                and num < height_map[i + 1][n]
            ):
                low_points.append(num)
        elif i == 0:
            if n == 0:
                if num < row[n + 1] and num < height_map[i + 1][n]:
                    low_points.append(num)
            elif n == len(row) - 1:
                if num < row[n - 1] and num < height_map[i + 1][n]:
                    low_points.append(num)
            elif num < row[n - 1] and num < row[n + 1] and num < height_map[i + 1][n]:
                low_points.append(num)

        elif i == len(height_map) - 1:
            if n == 0:
                if num < row[n + 1] and num < height_map[i - 1][n]:
                    low_points.append(num)
            elif n == len(row) - 1:
                if num < row[n - 1] and num < height_map[i - 1][n]:
                    low_points.append(num)
            elif num < row[n - 1] and num < row[n + 1] and num < height_map[i - 1][n]:
                low_points.append(num)
        elif n == 0:
            if (
                num < row[n + 1]
                and num < height_map[i - 1][n]
                and num < height_map[i + 1][n]
            ):
                low_points.append(num)
        elif n == len(row) - 1:
            if (
                num < row[n - 1]
                and num < height_map[i - 1][n]
                and num < height_map[i + 1][n]
            ):
                low_points.append(num)

print(sum(low_points) + len(low_points))

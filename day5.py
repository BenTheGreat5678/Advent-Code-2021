with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums.readlines()]

coord_list = [num.split(" -> ") for num in num_list]
line_list = []

for set_xy in coord_list:

    if (
        set_xy[0].split(",")[0] == set_xy[1].split(",")[0]
        or set_xy[0].split(",")[1] == set_xy[1].split(",")[1]
    ):
        x1 = int(set_xy[0].split(",")[0])
        x2 = int(set_xy[1].split(",")[0])
        y1 = int(set_xy[0].split(",")[1])
        y2 = int(set_xy[1].split(",")[1])

        if x2 > x1:  # Y is constant
            for i in range(x1, x2 + 1):
                line_list.append(f"{i},{y1}")

        elif x1 > x2:
            for i in range(x1, x2 - 1, -1):
                line_list.append(f"{i},{y1}")

        elif y2 > y1:  # X is constant
            for i in range(y1, y2 + 1):
                line_list.append(f"{x1},{i}")

        elif y1 > y2:
            for i in range(y1, y2 - 1, -1):
                line_list.append(f"{x1},{i}")

        elif x1 == x2 and y1 == y2:
            line_list.append(f"{x1},{y1}")
    elif abs(int(set_xy[0].split(",")[0]) - int(set_xy[1].split(",")[0])) == abs(
        int(set_xy[0].split(",")[1]) - int(set_xy[1].split(",")[1])
    ):
        x1 = int(set_xy[0].split(",")[0])
        x2 = int(set_xy[1].split(",")[0])
        y1 = int(set_xy[0].split(",")[1])
        y2 = int(set_xy[1].split(",")[1])

        if x2 > x1 and y2 > y1:
            x_list = [i for i in range(x1, x2 + 1)]
            y_list = [n for n in range(y1, y2 + 1)]
            for index, num in enumerate(x_list):
                line_list.append(f"{num},{y_list[index]}")

        elif x2 < x1 and y2 < y1:
            x_list = [i for i in range(x1, x2 - 1, -1)]
            y_list = [n for n in range(y1, y2 - 1, -1)]
            for index, num in enumerate(x_list):
                line_list.append(f"{num},{y_list[index]}")

        elif x2 > x1 and y2 < y1:
            x_list = [i for i in range(x1, x2 + 1)]
            y_list = [n for n in range(y1, y2 - 1, -1)]
            for index, num in enumerate(x_list):
                line_list.append(f"{num},{y_list[index]}")

        elif x2 < x1 and y2 > y1:
            x_list = [i for i in range(x1, x2 - 1, -1)]
            y_list = [n for n in range(y1, y2 + 1)]
            for index, num in enumerate(x_list):
                line_list.append(f"{num},{y_list[index]}")

used_list = []
danger_spots = 0
for coord in line_list:
    count = line_list.count(coord)
    if count > 1:
        if coord not in used_list:
            used_list.append(coord)
            danger_spots += 1
print(danger_spots)

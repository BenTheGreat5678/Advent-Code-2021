with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums.readlines()]

position = 0
depth = 0
aim = 0

for dir in num_list:
    dir_num = dir.split()
    if dir_num[0] == "forward":
        position += int(dir_num[1])
        depth += aim * int(dir_num[1])
    elif dir_num[0] == "down":
        aim += int(dir_num[1])
    else:
        aim -= int(dir_num[1])

print(position * depth)

# 1960569556

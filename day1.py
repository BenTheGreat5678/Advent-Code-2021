with open("advent_data.txt") as nums:
    num_list = [int(num.replace("\n", "")) for num in nums.readlines()]

sum_list = [
    num_list[i] + num_list[i + 1] + num_list[i + 2]
    for i in range(len(num_list))
    if i + 2 < len(num_list)
]

increment = 0

for i in range(len(sum_list)):
    if sum_list[i - 1] < sum_list[i]:
        increment += 1

print(increment)

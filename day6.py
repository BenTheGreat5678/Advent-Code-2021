with open("advent_data.txt") as nums:
    num = nums.readlines()
numbs = num[0].split(",")
num_list = [int(chr) for chr in numbs]


for i in range(80):

    for num in num_list:
        if num == 0:
            num_list.append(int(9))
            num = 7
    num_list = [num - 1 for num in num_list]
    print(num_list)

print(len(num_list))

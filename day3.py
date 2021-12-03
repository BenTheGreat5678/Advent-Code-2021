with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums.readlines()]


gamma_rate = []
epsilon_rate = []

for i in range(len(num_list[0])):
    chr_list = []
    for num in num_list:
        chr_list.append(num[i])

    if chr_list.count("1") > chr_list.count("0"):
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")

print(int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2))

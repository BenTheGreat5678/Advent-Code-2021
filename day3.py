with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums.readlines()]


def o2_recursion(o2_list: list, factor):
    if len(o2_list) == 1:
        return o2_list

    chr_list = []
    for binary in o2_list:
        chr_list.append(binary[factor])

    if chr_list.count("1") >= chr_list.count("0"):
        o2_list = [num for num in o2_list if num[factor] == "1"]

    else:
        o2_list = [num for num in o2_list if num[factor] == "0"]

    return o2_recursion(o2_list, factor + 1)


def co2_recursion(co2_list: list, factor):
    if len(co2_list) == 1:
        return co2_list

    chr_list = []
    for chr in co2_list:
        chr_list.append(chr[factor])

    if chr_list.count("1") >= chr_list.count("0"):
        co2_list = [num for num in co2_list if num[factor] == "0"]
    else:
        co2_list = [num for num in co2_list if num[factor] == "1"]

    return co2_recursion(co2_list, factor + 1)


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

o2_gen = []
co2_scrub = []

chr_list = []
for binary in num_list:
    chr_list.append(binary[0])

if chr_list.count("1") >= chr_list.count("0"):
    for num in num_list:
        if num[0] == "1":
            o2_gen.append(num)
        else:
            co2_scrub.append(num)
else:
    for num in num_list:
        if num[0] == "0":
            o2_gen.append(num)
        else:
            co2_scrub.append(num)

ox_gen = o2_recursion(o2_gen, 1)
co2_scrub = co2_recursion(co2_scrub, 1)
print(ox_gen)
print(co2_scrub)

print(int("".join(ox_gen), 2) * int("".join(co2_scrub), 2))

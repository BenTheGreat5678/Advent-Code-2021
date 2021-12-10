with open("advent_data.txt") as nums:
    num = nums.readlines()
num_list = num[0].split(",")
num_list = [int(num) for num in num_list]


for i in range(min(num_list), max(num_list) + 1):
    fuel_cost = []
    for ship in num_list:
        fuel_cost.append(sum(range(1, abs(ship - i) + 1)))

    if i == min(num_list):
        min_fuel = sum(fuel_cost)
    elif sum(fuel_cost) < min_fuel:
        min_fuel = sum(fuel_cost)


print(min_fuel)

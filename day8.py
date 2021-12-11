with open("advent_data.txt") as nums:
    num = [num.replace("\n", "") for num in nums.readlines()]

code_digits = []
segment_digits = []
for i in num:
    code_digits.append(i.split("|")[1])
    segment_digits.append(i.split("|")[0])

#      1
# 2         3
#      4
# 5         6
#      7
final_strs = []

for ind, combo in enumerate(num):
    segment_dict = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}

    for code in segment_digits[ind].split():

        if len(code) == 2:
            segment_dict[3] = code
            segment_dict[6] = code
        elif len(code) == 3:
            segment_dict[1] = code
        elif len(code) == 4:
            segment_dict[2] = code
            segment_dict[4] = code
        elif len(code) == 7:

            segment_dict[5] = code
            segment_dict[7] = code

    for i in segment_dict[3]:
        segment_dict[1] = segment_dict[1].replace(i, "")
        segment_dict[2] = segment_dict[2].replace(i, "")
        segment_dict[4] = segment_dict[4].replace(i, "")
        segment_dict[5] = segment_dict[5].replace(i, "")
        segment_dict[7] = segment_dict[7].replace(i, "")

    segment_dict[5] = segment_dict[5].replace(segment_dict[1], "")
    segment_dict[7] = segment_dict[7].replace(segment_dict[1], "")

    for i in range(len(segment_dict[2])):
        segment_dict[5] = segment_dict[5].replace(segment_dict[2][i], "")
        segment_dict[7] = segment_dict[7].replace(segment_dict[2][i], "")

    for code in segment_digits[ind].split():
        if len(code) == 5:
            if segment_dict[3][0] in code and segment_dict[3][1] in code:
                for i, num in enumerate(segment_dict[4]):
                    if num in code:
                        segment_dict[2] = segment_dict[2].replace(
                            segment_dict[2][i], ""
                        )
                        for key, code2 in segment_dict.items():
                            if num in code2:
                                segment_dict[key] = num
                        break

                for i, num in enumerate(segment_dict[7]):
                    if num in code:
                        segment_dict[5] = segment_dict[5].replace(
                            segment_dict[5][i], ""
                        )
                        for key, code2 in segment_dict.items():
                            if num in code2:
                                segment_dict[key] = num
                        break

    for code in segment_digits[ind].split():
        if len(code) == 5:
            if segment_dict[2] in code:
                for num in segment_dict[6]:
                    if num in code:
                        segment_dict[3] = segment_dict[3].replace(num, "")
                    else:
                        segment_dict[6] = segment_dict[6].replace(num, "")

    final_string = ""

    for code in code_digits[ind].split():

        if len(code) == 7:
            final_string += "8"
        elif len(code) == 2:
            final_string += "1"
        elif len(code) == 3:
            final_string += "7"
        elif len(code) == 4:
            final_string += "4"
        else:
            code_list = []
            for i in code:
                code_list.append(i)
            code_list.sort()
            if len(code) == 5:
                two_sort = [
                    segment_dict[1],
                    segment_dict[3],
                    segment_dict[4],
                    segment_dict[5],
                    segment_dict[7],
                ]
                three_sort = [
                    segment_dict[1],
                    segment_dict[3],
                    segment_dict[4],
                    segment_dict[6],
                    segment_dict[7],
                ]
                five_sort = [
                    segment_dict[1],
                    segment_dict[2],
                    segment_dict[4],
                    segment_dict[6],
                    segment_dict[7],
                ]
                two_sort.sort()
                three_sort.sort()
                five_sort.sort()
                if code_list == two_sort:
                    final_string += "2"
                elif code_list == five_sort:
                    final_string += "5"
                elif code_list == three_sort:
                    final_string += "3"
            if len(code) == 6:
                six_sort = [
                    segment_dict[1],
                    segment_dict[2],
                    segment_dict[4],
                    segment_dict[5],
                    segment_dict[6],
                    segment_dict[7],
                ]
                nine_sort = [
                    segment_dict[1],
                    segment_dict[2],
                    segment_dict[3],
                    segment_dict[4],
                    segment_dict[6],
                    segment_dict[7],
                ]
                zero_sort = [
                    segment_dict[1],
                    segment_dict[2],
                    segment_dict[3],
                    segment_dict[5],
                    segment_dict[6],
                    segment_dict[7],
                ]
                zero_sort.sort()
                six_sort.sort()
                nine_sort.sort()
                if code_list == zero_sort:
                    final_string += "0"
                elif code_list == six_sort:
                    final_string += "6"
                elif code_list == nine_sort:
                    final_string += "9"
    final_strs.append(int(final_string))
print(final_strs)
print(sum(final_strs))

# num_unique = 0

# for codes in code_digits:
#     for code in codes.split():

#         if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7:
#             num_unique += 1

# print(num_unique)

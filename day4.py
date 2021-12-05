import numpy as np

with open("advent_data.txt") as nums:
    num_list = [num.replace("\n", "") for num in nums.readlines()]

end_list = []
bingo_cards = []
winner_card = []

bingo_nums = num_list[0]
num_list.pop(0)
num_list.pop(0)
num_list = list(filter(None, num_list))

for row in num_list:
    chr_list = [int(num) for num in row.split()]
    end_list.append(chr_list)

for i in range(len(num_list) // 5):
    bingo_cards.append(end_list[i * 5 : (i * 5) + 5])
    

# for card in bingo_cards:
#     for row in card:
#         print(row)
#     print('\n\n')

complete_cards = 0
won_cards = []

for play_num in bingo_nums.split(','):
    for i, card in enumerate(bingo_cards):
        for n, row in enumerate(card):
            if int(play_num) in row:
                index = row.index(int(play_num))
                bingo_cards[i][n].remove(int(play_num))
                bingo_cards[i][n].insert(index, 'x')

            # Part 1
            # if len(set(row)) == 1:
            #     win_card = i
            #     win_num = play_num
            #     break
            
            # for c in range(5):
            #     if len(set(np.array(card)[:,c])) == 1:
            #         win_card = i
            #         win_num = play_num
            #         break

            if len(set(row)) == 1:
                if card not in won_cards:
                    won_cards.append(card)
                    complete_cards += 1
                
            for c in range(5):
                if len(set(np.array(card)[:,c])) == 1:
                    if card not in won_cards:
                        won_cards.append(card)
                        complete_cards += 1
                        break


            if complete_cards == len(bingo_cards):
                last_num = play_num
                last_card = i
                break

            # Part 1
            # else:
            #     continue
            # break
        else:
            continue
        break
    else:
        continue
    break

final_sum = 0

# for card in bingo_cards:
#     for row in card:
#         print(row)
#     print('\n\n')

# Part 1
# for row in bingo_cards[win_card]:
#     for chr in row:
#         if chr != 'x':
#             final_sum += chr
# print(final_sum * int(win_num))

for row in bingo_cards[last_card]:
    for chr in row:
        if chr != 'x':
            final_sum += chr

print(final_sum * int(last_num))
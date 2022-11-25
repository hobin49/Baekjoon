# n = input()

# card = [0] * 10

# for i in str(n):
#     if i == "6" or i == "9":
#         if card[6] == card[9]:
#             card[6] += 1
#         else:
#             card[9] += 1

#     else:
#         card[int(i)] += 1
# print(card)
# print(max(card))

from collections import Counter

n = dict(Counter(input()))

n["6"] = (n.get("6", 0) + n.get("9", 0) + 1) // 2
n["9"] = 0

print(max(n.values()))

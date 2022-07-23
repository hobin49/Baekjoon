import sys


input = sys.stdin.readline

n = int(input())
his_cards = list(map(int, input().split()))
m = int(input())
check_cards = list(map(int, input().split()))


dictionary = {}

for i in his_cards:
    dictionary[i] = dictionary.get(i, 0) + 1

for j in check_cards:
    if j in dictionary:
        print(dictionary[j], end = " ")
    else:
        print(0, end = " ")
    
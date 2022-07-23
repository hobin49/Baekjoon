import sys
input = sys.stdin.readline
# 상근이가 가지고 있는 카드의 개수
n = int(input())

# 상근이의 숫자 카드들
sangeun_card = list(map(int, input().split()))
# 비교 할 숫자카드의 수
m = int(input())

#비교 할 숫자 카드들
card_number = list(map(int, input().split()))

#list to dict
dictionary = {c : 0 for c in card_number}
dictionary_2 = {d for d in sangeun_card}



for key,value in dictionary.items():
    if key in dictionary_2:
        print(1, end = " ")
    else:
        print(0, end = " ")

#         print(1, end = "")
#     else:
#         print(0, end = "")

# 다른분 풀이 (best)
import sys

input = sys.stdin.readline

#상근이가 가지고 있는 카드의 개수
n = int(input())

#상근이의 숫자 카드들
n_cards = list(map(int, input().split()))

#비교 할 숫자카드의 개수
m = int(input())

#비교 할 숫자카드들
m_cards = list(map(int, input().split()))

#정답을 넣을 딕셔너리
dictionary = {}

for i in n_cards:
    # n_cards 들의 갯수 파악
    dictionary[i] = dictionary.get(i, 0) + 1

for i in m_cards:
    # 만약 dictionary 안에 i값이 있으면 그에 대한 개수를 보여줌
    if i in dictionary:
        print(dictionary[i], end=" ")
    # 없으면 0 으로 출력
    else:
        print(0, end=" ")
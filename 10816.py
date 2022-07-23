import sys


input = sys.stdin.readline

n = int(input())
his_cards = list(map(int, input().split()))
m = int(input())
check_cards = list(map(int, input().split()))


dictionary = {} #빈 딕셔너리를 만들고 

for i in his_cards:
    dictionary[i] = dictionary.get(i, 0) + 1 # get 메서드를 사용해서 key와 value를 넣고

for j in check_cards: # check_cards의 리스트를 돌고
    if j in dictionary: # 만약에 딕셔너리에 있다면
        print(dictionary[j], end = " ") #해당 딕셔너리의 value값을 print
    else:
        print(0, end = " ") #없으면 0을 출력
    
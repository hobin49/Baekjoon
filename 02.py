import sys

sys.stdin = open("02_input.txt", "r")

dictionary = {'b': 'd', 'd':'b', 'p': 'q', 'q': 'p'} #거울에 반사되는 문자열을 담은 딕셔너리
for tc in range(1, int(input())+1):
    alphabet = input() #입력값을 리스트에 받아온다 #리스트를 굳이 쓰지 않아도 돼!!
    result = "" #결과값 받을 변수

    for alpha in alphabet: #입력값들을 for문을 돌아주면서
        if alpha in dictionary:
            result += dictionary[alpha]

    print(f"#{tc} {result[::-1]}")

t = int(input())
cereal = []
#입력값 받기
for _ in range(t):
    alpha = input()
    cereal.append(alpha)

#딕셔너리를 활용
dictionary = {}
#2번 조건 자리수의 합을 비교하기 위한 과정
for c in cereal:
    number = [int(s) for s in c if s.isdigit()]
    #길이와 각 자릿수의 합을 구해서 딕셔너리에 넣는다 
    dictionary[c] = [len(c),sum(number)]
#딕셔너리 value에 길이, 자릿수, 사전순으로 정렬한다.
dictionary = sorted(dictionary.items(), key=lambda x:(x[1][0], x[1][1], x[0]))

#출력
for d in dictionary:
    print(d[0])

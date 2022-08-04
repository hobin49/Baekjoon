import sys 
input = sys.stdin.readline
N = int(input())
dictionary = {} # 딕셔너리 만들어주고
for i in range(N):
    name = input()
    if name not in dictionary:
        dictionary[name] = 1
    else: #동명이인시
        dictionary[name] += 1

for j in range(N-1):
    name = input()
    dictionary[name] -= 1 #완주한 이름은 -1


for key, value in dictionary.items(): # items의 메서드를 사용해서 value가 1개라도 있으면
    if value != 0:
        print(key)# key를 출력
        break


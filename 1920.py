import sys 

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dictionary = {}

for i in n_list:
    dictionary[i] = dictionary.get(i, 0) + 1

for j in m_list:
    if j in dictionary:
        print(1)
    else:
        print(0)

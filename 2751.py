import sys
input = sys.stdin.readline
T = int(input())
numbers = []
for s in range(T):
    a = (int(input()))
    numbers.append(a)
numbers.sort() # for문 안에서 수행하면 시간 초과가 뜬다. 
               # sort()메서드는 O(nlogn)이 걸린다. 근데 그게 for문 안에 들어가면
               # n * nlogn이 된다.
for k in numbers:
    print(k)
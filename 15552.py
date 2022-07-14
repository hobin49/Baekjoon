import sys
T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split()) #sys.stdin.readline()은 여러줄을 입력 받아야 할 때는 input()를 입력 받으면 시간초과
    print(A + B)
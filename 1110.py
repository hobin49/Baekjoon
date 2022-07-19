N = int(input())

M = 0
c = N
cycle = 1
M = (N // 10) + (N % 10)
N = int(str((N % 10)) + str(M % 10))

while c != N:
    M = (N // 10) + (N % 10)
    N = int(str((N % 10)) + str(M % 10))
    cycle += 1

print(cycle)
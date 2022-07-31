
M = []

for i in range(int(input())):
    M.append(int(input()))



k = sorted(M) # for문 밖에서 정렬해주고 
print(*k, sep="\n") # 언팩킹
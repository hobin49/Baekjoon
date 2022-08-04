
M = []

for i in range(int(input())):
    M.append(int(input()))



k = sorted(M) # for문 밖에서 정렬해주고 
print(*k, sep="\n") # 언팩킹



# # 다른 분 풀이 힙 활용
# import heapq

# N = int(input())
# arr = []

# for i in range(N):
#     number = int(input())
#     heapq.heappush(arr, number)

# for j in range(N):
#     print(heapq.heappop(arr))
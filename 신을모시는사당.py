# n = int(input())
# lst = list(map(int, input().split()))

# #누적합 구할 리스트가 필요
# sum_ = [0 for _ in range(n+1)]


# s = 0
# result = []
# for i in range(n):
#     if lst[i] == 1:
#         s += 1
#         sum_.append(s)
#     elif lst[i] == 2:
#         s -= 1
#         sum_.append(s)

# # 0 -(-4) = 4
# print(max(sum_) - min(sum_))

# n = int(input())
# direc = list(map(int, input().split()))
# ans = [0] * n

# cnt = 0

# for i in range(n):
#     if direc[i] == 1:
#         cnt +=1
#     else:
#         cnt -=1
#     ans.append(cnt)

# print(max(ans) - min(ans))


n = int(input())

lst = list(map(int, input().split()))

m = [n, -n]

k = 0

for i in range(n):
    if lst[i] == 1:
        k += 1
    else:
        k -= 1

    if k < m[0]:
        m[0] = k
    else:
        m[1] = k

if m[0] > 0:
    m[0] = 0

if m[1] < 0:
    m[1] = 0

print(m[1] - m[0])

ans = []
k = 0
for _ in range(4):
    n, m = map(int, input().split())
    k += m - n
    ans.append(k)

print(max(ans))

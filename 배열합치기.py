n, m = map(int, input().split())
lst = []
i = list(map(int, input().split()))
p = list(map(int, input().split()))

result = i + p

answer = sorted(result)

print(*answer)
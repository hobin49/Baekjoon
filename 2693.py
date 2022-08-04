
N = 3
result = []
for _ in range(int(input())):
    number = list(map(int, input().split()))
    a_sort = sorted(number, reverse=True)
    result.append(a_sort[N-1])

print(*result, sep="\n")
D, N = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

for i in range(1, D):
    oven[i] = min(oven[i], oven[i - 1])

print(oven)

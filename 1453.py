N = int(input())

seat = list(map(int, input().split()))
s = len(list(set(seat)))

print(N - s)



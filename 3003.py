piece = [1, 1, 2, 2, 2, 8]

chess = list(map(int, input().split()))

result = [x - y for x, y in zip(piece, chess)]

print(*result)
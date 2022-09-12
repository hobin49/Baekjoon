n, m = map(int, input().split())

k = list(map(int, input().split()))

k.sort()

print(k[m-1])
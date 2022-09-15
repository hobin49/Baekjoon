n, m = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number, reverse=True)

print(number[m-1])
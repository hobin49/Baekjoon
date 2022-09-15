t = int(input())
for _ in range(t):
    number = list(map(int, input().split()))
    number.remove(max(number))
    number.remove(min(number))
    if max(number) - min(number) >= 4:
        print("KIN")
    else:
        print(sum(number))
    
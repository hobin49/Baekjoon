t = int(input())
for _ in range(t):
    number = input()
    n = int(number) + int(number[::-1])
    n_reverse = str(n)
    if str(n) == n_reverse[::-1]:
        print("YES")
    else:
        print("NO")

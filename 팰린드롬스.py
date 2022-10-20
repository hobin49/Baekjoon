t = int(input())
for _ in range(t):
    n = input().lower()
    if n[::-1] == n:
        print("Yes")
    else:
        print("No")

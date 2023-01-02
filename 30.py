n = int(input())
data = []
k = list(str(n))
k_number = "".join(sorted(k, reverse=True))


if int(k_number) % 30 == 0:
    print(k_number)

else:
    print(-1)

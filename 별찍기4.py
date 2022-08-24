# n = int(input())
# for i in range(n, -1, -1):
#     print(("*" * i).rjust(n))


## 다른 방법
n = 5
for i in range(n, -1, -1):
    print(" " * (n-i) + "*" * i)
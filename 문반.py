n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    str_ = ""
    for i in b:
        str_ += i * int(a)

    print(str_)

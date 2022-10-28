n = int(input())

for _ in range(n):
    m = int(input())
    lst = []
    for _ in range(m):
        number = input()
        lst.append(number)
        lst.sort()

    for i in range(m - 1):
        if lst[i] in lst[i + 1]:

            print("NO")
            break
    else:
        print("YES")

# import sys

# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     lst = []
#     n = int(input())
#     number = [input().rstrip() for _ in range(n)]
#     number.sort()

#     # 뒤에 두개만 보면 돼
#     for i in range(n - 1):
#         if number[i + 1].startswith(number[i]):
#             print("NO")
#             break
#     else:
#         print("YES")

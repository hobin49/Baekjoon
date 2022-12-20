# n = list(map(str, input()))
# result = []
# for i in range(len(n)):
#     if n[i] == "-":
#         h = "".join((n[:i]))
#         k = list(n[i + 1 :])

#         for j in range(len(k)):
#             if k[j] == "+":
#                 a = "".join(k[:j])
#                 b = "".join(k[j + 1 :])
#                 print(int(a) + int(b) - int(h))


# ['55', '50+40']
a = input().split("-")
num = []
# 리스트가 2개로 되어있어
for i in a:
    cnt = 0
    # ['55'], ['50', '40']
    s = i.split("+")
    for j in s:
        cnt += int(j)
    num.append(cnt)
# 55
n = num[0]
for i in range(1, len(num)):
    # 55 -90
    n -= num[i]
print(n)

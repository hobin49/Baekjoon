n, m = map(int, input().split())

arr = []
# 문자열을 list 형식으로 담아준다.
for i in range(n):
    arr.append(list(map(str, input())))


cnt = 0
result = ""

# 행렬을 바꾼다.
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        # 많이 나온 개수를 샌다.
        if arr[j][i] == "T":
            t += 1
        elif arr[j][i] == "A":
            a += 1
        elif arr[j][i] == "G":
            g += 1
        elif arr[j][i] == "C":
            c += 1
    # 알파벳 순서대로 안하면 꼬인다.
    if max(a, c, g, t) == a:
        result += "A"
        cnt += c + g + t
    elif max(a, c, g, t) == c:
        result += "C"
        cnt += a + g + t
    elif max(a, c, g, t) == g:
        result += "G"
        cnt += a + c + t
    elif max(a, c, g, t) == t:
        result += "T"
        cnt += c + g + a

print(result)
print(cnt)

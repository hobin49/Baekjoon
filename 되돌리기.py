n = int(input())
k = []
for _ in range(n):
    k.append(list(map(str, input().split())))


lst = [("", "0")]
alpha = ""
for i in range(len(k)):
    if k[i][0] == "type":
        alpha += k[i][1]
        lst.append((alpha, k[i][2]))
    elif k[i][0] == "undo":
        lst.append()

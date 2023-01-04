n = int(input())

for _ in range(n):
    k = int(input())
    lst = []
    dictionary = {}
    for _ in range(k):
        lst.append(list(map(str, input().split())))

    for c, t in lst:
        if t not in dictionary:
            dictionary[t] = 2
        else:
            dictionary[t] += 1
    cnt = 1
    for num in dictionary.values():
        cnt *= num

    print(cnt - 1)

a = list(map(int, input()))

a.sort(reverse=True)
for reverse in a:
    print(reverse, end = "")
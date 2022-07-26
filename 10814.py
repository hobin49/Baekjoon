N = int(input())
for tc in range(N):
    name = list(map(str, input().split()))

name.sort(key=lambda x: (x[0], x[1]))

for person in name:
    print(person[0], person[1])
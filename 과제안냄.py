number = [i for i in range(1, 31)]

lst = []
n = 0
while n != 28:
    k = int(input())
    lst.append(k)
    n += 1

for num in lst:
    if num in number:
        number.remove(num)

print(*number, sep="\n")
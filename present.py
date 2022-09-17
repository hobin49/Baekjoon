t = int(input())
p = []
for _ in range(t):
    price = input()
    p.append(price)
p_list = sorted(p, key =float)
print(p_list[1])
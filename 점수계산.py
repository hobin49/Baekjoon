lst = []
idx = []
for i in range(1, 9):
   n = int(input())
   lst.append([n, i])
lst = sorted(lst, key=lambda x: x[0], reverse=True)
sum_ = []
idx = []
for k, j in lst[:5]:
    sum_.append(k)
    idx.append(j)
print(sum(sum_))
idx.sort()
print(*idx)



lst = []
for i in range(1, 10):
    lst.append(int(input()))
max_num = max(lst)
result = lst.index(max_num) +1

print(max_num, result)
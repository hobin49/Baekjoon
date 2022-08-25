sum_ = 0
lst = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        lst.append(n)
    
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))

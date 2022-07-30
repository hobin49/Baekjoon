result = []
n, m = map(int, input().split())
k = 1
while len(result) < m:
    for _ in range(k):
        result.append(k)
    
    k += 1

listslice = result[int(n)-1:int(m)]
print(sum(listslice))
T = int(input())

for _ in range(T):
    n = int(input())
    k = int(input())
    
    room = [i for i in range(1, k+1)]
    for j in range(n):
        for q in range(1, k):
            room[q] += room[q-1]
    print(room)

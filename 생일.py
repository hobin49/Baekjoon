from datetime import datetime
T = int(input())
names =[]
births = []
for _ in range(T):
    s = list(map(str, input().split()))
    name = s[0]
    names.append(name)
    b = s[1:]
    birth = "-".join(b)
    births.append(birth)

dictionary = dict(zip(names, births))
n_dict = sorted(dictionary.items(), key = lambda x:datetime.strptime(x, '%d-%m-%Y'))
print(*n_dict[-1][0], sep="")
print(*n_dict[0][0], sep="")


#다른 풀이 베스트
lst = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    lst.append([n, int(d), int(m), int(y)])
#lambda를 활용해서 우선순위 3-2-1순으로 오름차순 정렬한다. 
lst.sort(key=lambda x:(x[3], x[2], x[1]))

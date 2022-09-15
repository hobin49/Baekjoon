n = int(input())

result = []
ranking = [] # 등수정보를 저장할 리스트 ranking
for i in range(n):
    result.append(list(map(int, input().split())))
 
for i in range(n):
    count = 1
    for j in range(n):
        if result[i][0] < result[j][0] and result[i][1] < result[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
            print(count)
    ranking.append(count) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
print(ranking)
# for d in ranking:
#     print(d,end=" ")
#입력값을 받아준다.
from itertools import count


n = int(input())
#촌수를 계산해야 하는 서로 다른 두 사람의 번호
start , end = map(int, input().split())

#부모 자식들 간의 관계의 계수
m = int(input())

#인접리스트 형식 만들기
graph = [[] for _ in range(n + 1)]

#무방향 인접리스트 만들기
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

#방문 표시할 체크리스트를 만들기
visited = [False] * (n + 1)

#스택을 만들어준다. 출발값과 촌수 계산을 위한 초기값을 넣어준다.
stack = [(start, 0)]

#출발 노드를 방문 설정해준다.
visited[start] = True

#정답을 출력할 변수(촌수 계산을 할 수 없을 때 -1)
answer = -1

#스택에 비어있지 않을 떄까지 돌아준다.
while stack:
    #번호와 촌수를 같이 pop해준다.
    number, cnt = stack.pop()
    #만약 pop한 값이 우리가 원하는 값과 일치한다면 
    if number == end:
        #정답을 출력할 변수에 count한 값을 담아주고 종료한다.
        answer = cnt
        break
    
    #인접 노드를 돌면서
    for adj in graph[number]:
        #방문하지 않은 노드면 방문처리하고
        if not visited[adj]:
            visited[adj] = True
            #stack에 인접한 노드와 count + 1을 해줘서 촌수를 계산한다.
            stack.append((adj, cnt + 1))


#정답을 출력한다.
print(answer)
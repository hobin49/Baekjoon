n = int(input())
nodes = list(map(int, input().split()))
delete_node = int(input())
tree = [[] for _ in range(n)]

for i in range(n):
    if nodes[i] == -1:
        # -1이라면 루트노드이기 때문에 변수에 담아둔다.
        root = i
        # 무시
        continue
    # 이 처리를 하지 않으면 delete 노드가 리스트에 들어가게 된다.
    if i == delete_node:
        # 무시
        continue
    # tree에 들어갈 값은 루트노드와 삭제할 노드를 제외한 값들이 들어간다. 즉 지워질 값들의 인덱스
    # 예제 1번의 경우는 [[1], [3, 4], [], [], []]
    tree[nodes[i]].append(i)

answer = 0
# 함수를 돌자!
def dfs(node):
    # count해준 값을 나주엥 출력해야 하므로 전역변수를 사용
    global answer
    # 노드를 타고 밑으로 내려가서
    if tree[node]:
        # 만약에 tree에 다른 요소가 있으면 dfs를 또 돌려준다
        for i in tree[node]:
            # tree = [[1], [3, 4], [], [], []]
            # 1. (node = 0 i = 1) 2. (node=1 i=3) 3.(node=3, return None answer +=1)
            # 4. (node=1 i=4) 5.(node=4 return None answer += 1)
            dfs(i)
    # 더 이상 연결된 노드가 없다면 즉 리프노드인 경우 answer += 1
    else:
        answer += 1


# 예제 3번 입력에
# 5
# -1 0 0 1 1
# 0
# 여기서 루트노드가 지울 노드면 0이 나와야 하는데 이 조건이 없이 그냥 dfs(root)를 하면 3이 나온다.
if root != delete_node:
    dfs(root)
print(answer)

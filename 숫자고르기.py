# n = int(input())
# dic = {}

# for i in range(n):
#     dic[i + 1] = int(input())

# while True:
#     baseset = set(dic.values())
#     print(baseset)
#     dic = {key: value for key, value in dic.items() if key in baseset}
#     print(dic)
#     if baseset == set(dic.values()):
#         break

# print(len(dic))
# for key in dic.keys():
#     print(key)


import sys

input = sys.stdin.readline

N = int(input())
numbers = [0]

# 입력값을 받아준다.
for _ in range(N):
    numbers.append(int(input()))
# 중복 처리를 위해서 set을 활용
answer = set()

# dfs 함수
def dfs(index, first, second):
    # 1번째꺼는 1~n까지의 숫자
    first.add(index)
    # 2번째는 입력값 받은 값들
    second.add(numbers[index])

    # number의 값들이 1~n숫자 안에 있고
    if numbers[index] in first:
        # 같은 요소가 있는지 체크
        if first == second:
            # set에 추가해준다.
            answer.update(first)
        return
    return dfs(numbers[index], first, second)


for i in range(1, N + 1):
    # 돌지 않은 부분 있으면 다 돌아준다.
    if i not in answer:
        dfs(i, set(), set())

print(len(answer))
final = sorted(list(answer))


for number in final:
    print(number)

from collections import deque # deque를 쓰면 큐보다 빠르다

n = int(input())


queue = deque(range(1, n + 1)) #deque로 형변환

while len(queue) > 1: #queue의 길이가 1볻가 크다면 계속 돈다.
    print(queue.popleft(), end= " ") # 1,3,5,7 순서로 빼주고
    queue.append(queue.popleft()) # 2,4,6 은 뒤로 빼준다.

print(queue[0])


# n = int(input())

queue = list(range(1, n + 1))

while len(queue) > 1:
    print(queue.pop(0), end = " ")
    queue.append(queue.pop(0))

print(queue[0])

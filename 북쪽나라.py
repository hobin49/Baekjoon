from collections import defaultdict

graph = []

# 입력값 받기
while True:
    try:
        city1, city2, length = map(int, input().split())
        graph[city1].append((length, city2))
        graph[city2].append((length, city1))
    except:
        break

import sys
input = sys.stdin.readline
dictionary = {}
for _ in range(int(input())):
    name, record = input().split()
    dictionary[name] = record #dictionary에 key value값을 넣는다
for key, value in list(dictionary.items()): #Runtime error 방지하기 위해 list에 덮어쓰임
    if value == "leave":
        del dictionary[key]

result= sorted(dictionary.keys(), reverse=True)

print(*result, sep= "\n")
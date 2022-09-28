# 입력값 받고
n = int(input())
dict1 = {}
lst1 = []
# 테스만큼 돌면서
for i in range(n):
    # 입력값을 받고
    car_number = input()
    # 입력값을 리스트에 더하고
    lst1.append(car_number)
    # 딕셔너리에 value를 넣어주고
    dict1[lst1[i]] = i + 1

dict2 = {}
lst2 = []
for j in range(n):
    # 나머지 입력값을 또 받아주고
    car_number1 = input()
    # 리스트에 값을 더하고
    lst2.append(car_number1)
    # 딕셔너리에 value를 넣어주고
    dict2[lst2[j]] = j + 1

# 만약에 딕셔너리2 아이템들 중에
for key, value in dict2.items():
    # 같은 key가 dict1에 있으면
    if key in dict1.keys():
        # dict2의 value를 dict1의 value에 맞게 바꿔준다.
        dict2[key] = dict1[key]

# 여기서 생각한 부분 두 딕셔너리의 값들을 빼주고
result = [a - b for a, b in zip(dict1.values(), dict2.values())]

# 몇 대인지 세어줄 변수
cnt = 0
# 뺴준값들을 돌면서
for i in result:
    # 만약 음수이면 1씩 늘려준다.
    if i < 0:
        cnt += 1

print(cnt)

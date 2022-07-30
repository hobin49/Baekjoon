N = int(input())
membership = [] # 이름과 나이를 받을 리스트
for tc in range(N):
    age, name = map(str, input().split()) # 이름과 나를 받고
    age = int(age) # 나이를 str에서 int로 바꿔주고 
    membership.append((age, name)) # age를 int로 바꿔준 것을 리스트에 담는다


membership.sort(key=lambda x : x[0]) # 익명함수 lambda를 사용해서 0번째 인덱스들을 정렬

for member in membership:
    print(member[0], member[1]) #출력
from collections import Counter
numbers = []
T = int(input())
for tc in range(T):
    num = int(input()) #입력을 담을 변수
    numbers.append(num) #리스트에 추가

cnt = Counter(sorted(numbers)) #counter함수 사용해서 갯수 세어준다. #sorted함수로 정렬도 해준다
print(cnt.most_common(1)[0][0])#가장 큰 수의 key값을 출력
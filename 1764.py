n,m = map(int, input().split()) #n과 m을 입력 받고
name1 = set() #set함수 활용
for tc in range(n):
    name1.add(input()) #set에 add해준다

name2 = set() 
for tc1 in range(m):
    name2.add(input())

name_ = name1 & name2 #교집합을 변수에 담는다


print(len(name_), *sorted(name_), sep = "\n") # 길이와, 정렬해준 값, 개행써서 분리해준다.
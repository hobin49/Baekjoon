A = int(input())
B = int(input())
C = int(input())

three_multiple = str(A * B * C)

dictionary = {'0' : 0, '1': 0, '2' : 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, 
'8':0, '9': 0} #딕셔너리 초기값 설정

for num in three_multiple:
    dictionary[num] = dictionary.get(num, 0) +1 #get 메서드를 활용해서 해당 value를 증가

print(*dictionary.values(), sep="\n") #*쓰면 마치 여러 개의 인자를 넘긴 효과가 난다
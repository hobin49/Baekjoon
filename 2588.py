A = int(input())
B = int(input())

#입력값 str(B)를 int형태로 변환해주고 list안에 넣는다.
b_list = list(map(int, str(B)))

print(A * b_list[-1])
print(A * b_list[1])
print(A * b_list[0])
print(A * B)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0
sign = 0




for i in range(len(A)):
    if A[i] > B[i]:
        A_score += 3
        sign = 1
    elif A[i] == B[i]:
        A_score += 1
        B_score += 1
    else:
        B_score += 3
        sign = 2

print(A_score, B_score)

if A_score > B_score:
    print("A")
elif A_score < B_score:
    print("B")
else:
    if sign == 1:
        print("A")
    elif sign == 2:
        print("B")
    else:
        print("D")    
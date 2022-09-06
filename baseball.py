T = int(input())
for i in range(T):
    y_score = 0
    k_score = 0
    for j in range(9):
        y, k = map(int, input().split())
        if y > k:
            y_score += 1
        else:
            k_score += 1
    if y_score > k_score:
        print("Yonsei")
    elif y_score == k_score:
        print("Draw")
    else:
        print("Korea")

T = int(input())

# 테스트 케이스 수만큼의 두 수를 입력받는다. 
for _ in range(T):
    #두 수를 한 번만 입력받는 것이 아니고 맨 처음 테스트 케스 수만큼의 두 수를 입력받는 것이다.
    A, B = map(int, input().split())
    print(A + B)
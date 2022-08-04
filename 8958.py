T = int(input())


for test_case in range(1, T +1):
    quiz = input()
    answer = 0 #변수를 for문 안에서 써야한다. for문 밖에서 선언하면 값이 초기화가 안 된다.
    result = 0

    for ox in quiz: #quiz안을 돌면서
        if ox == 'O': # 0이 나오면
            answer += 1 # +1을 해주고
            result += answer # 그 값을 result에 더해주면 누적이 된다.
        else:
            answer = 0
    
    print(result)
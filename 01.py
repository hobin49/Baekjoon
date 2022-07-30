import sys

sys.stdin = open("01_input.txt", "r")

total_T = int(input())

for tc in range(1, total_T+1):
    part_T = int(input())
    scores = list(map(int, input().split())) # 리스트에 값을 넣어준다
    average = sum(scores) // len(scores) #리스트의 합을 리스트의 길이로 나눈다
    count = 0 # 평균 이하 소득을 가진 사람들을 세기 위한 변수

    for score in scores: #score을 돌면서
        if score <= average: # 점수가 평균보다 아래이면
            count += 1 # count += 1을 해서 세준다.
    
    print(f"#{tc} {count}")

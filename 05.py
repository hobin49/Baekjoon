import sys
sys.stdin = open("05_input.txt", "r")

T = int(input()) #입력 테스트케이스 받기

card_number = ['3', '4', '5', '6', '9'] # 시작 번호 담아 놓기
for tc in range(1, T+1):
    number = list(map(str, input())) # list에 입력 값을 담아준다
    
    result = ""
    for i in number: # number의 값들을 돌면서 #split("-")을 사용하면 없앨 수 있다.
        if "-" != i: # 만약에 "-"가 있으면
            result += i # 값을 제거해주고

    if number[0] in card_number and len(number) == 16: # 인덱스 첫번째가 시작 번호에 있거나 길이가 16이면
        print(f"#{tc} 1") # 1을 출력
    else:
        print(f"#{tc} 0") #그렇지 않으면 0을 출력
T = int(input())

for tc in range(1,1+T):
    
    # 3개의 숫자를 list에 담아준다
    square = sorted(list(map(int,input().split())))
 
 
    # 0번째 인덱스와 그 다음 인덱스가 불일치하면 서로 다른 값이기 때문에
    if square[0] != square[1]: 
        print(f'#{tc} {square[0]}') #0번째 인덱스의 값을 넣어주고 
    else:
        print(f'#{tc} {square[2]}') # 같다면 2번째 인덱스의 값이 다른 값이기에 출력해준다.

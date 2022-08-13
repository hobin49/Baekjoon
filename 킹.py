directions = {
    "T" : (-1, 1),
    "LT": (-1, -1),
    "L": (0, -1),
    "LB": (1, -1),
    "B": (1, 0),
    "RB": (1, 1),
    "R": (0, 1),
    "RT" : (-1,1)
}

#입력 값을 받아준다.
king, stone, n = input().split()

#움직여야 하는 방향 리스트를 받아준다. 형변환 해주기
moving = [input() for _ in range(int(n))]

#값을 치환해준다. #A1 -> (7, 0)
king1, king2 = 8 - int(king[1]), ord(king[0]) - 65
stone1, stone2 = 8 - int(stone[1]), ord(stone[0]) - 65

#딕셔너리를 활용해서 다음을 이동한다.
for i in range(len(moving)):
    move = directions[moving[i]]
    #킹이 다음 이동할 방향을 담아준다.
    nking1 = king1 + move[0]
    nking2 = king2 + move[1]
    #만약 이동할 방향이 체스판을 벗어나면 무시한다.
    if not(-1 < nking1 < 8 and -1 < nking2 < 8):
        continue
    
    # 다음 이동해야할 범위랑 돌이랑 겹치면 돌을 이동해준다.
    if nking1 == stone1 and nking2 == stone2:
        nstone1 = stone1 + move[0]
        nstone2 = stone2 + move[1]

        # 이동한 돌이 범위를 벗어나면 무시한다.
        if not(-1 < nstone1 < 8 and -1 < nstone2 < 8):
            continue
        #범위를 벗어나지 않으면 킹과 돌을 이동해준다
        else:
            king1, king2 = nking1, nking2
            stone1, stone2 = nstone1, nstone2
    # 돌이랑 겹쳐지도 않고 체스판도 벗어나지 않으면 킹이 이동한다.    
    else:
        king1, king2 = nking1, nking2

#이제 최종적으로 이동한 위치가 담긴 값을 다시 치환한다. (7, 0) -> A1
print(chr(ord("A") + king2) + str(8 - king1))
print(chr(ord("A") + stone2) + str(8 - stone1))

        
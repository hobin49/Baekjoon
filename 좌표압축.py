n = int(input())
#좌표 입력받기
coordinate = list(map(int, input().split()))
#정렬한 값들의 인덱스와 값을 받기 위한 리스트
c_index = []
#set함수 사용해서 중복 제거
set_coordinate = set(coordinate)
#set을 정렬하고
set_ = sorted(list(set_coordinate))
#enumerate를 사용해서 인덱스를 리스트에 추가해주고
for (i, v) in enumerate(set_):
    c_index.append((i, v))
#딕셔너리 형태로 바꿔주고 
dictionary = dict((x,y) for y, x in c_index)

#만약 입력값이 딕셔너리에 있으면
for c in coordinate:
    if c in dictionary.keys():
        #해당 value를 출력해준다.
        print(dictionary[c], end=" ")
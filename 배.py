n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

# 만약 박스 값이 크레인보다 크면 옮길 수 없는 박스이니 -1을 출력
if box[0] > crane[0]:
    print(-1)

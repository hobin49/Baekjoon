n, w, L = map(int, input().split())

truck_weights = list(map(int, input().split()))

#다리 길이만큼 리스트를 만들어준다.
bridge = [0] * w

#시간 측정할 변수 
time = 0

#while문을 사용해서 bridge가 없을때까지 코드를 돌린다.
while bridge:
    #bridge의 첫 번째 요소를 꺼낼때마다 시간을 측정한다.
    bridge.pop(0)
    time += 1
    #만약 트럭이 남아 있다면
    if len(truck_weights) != 0:
        #만약에 최대하중을 초과하지 않으면 트럭을 하나씩 차례대로 지나가게 해준다.
        if sum(bridge) + truck_weights[0] <= L:
            truck = truck_weights.pop(0)
            bridge.append(truck)

        #초과하면 bridge에 0을 추가한다. 
        else:
            bridge.append(0)

print(time)
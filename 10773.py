numbers = []
for i in range(int(input())):
    K = int(input())
    if K != 0: #입력 받은 수 0이 아니면 
        numbers.append(K) # 리스트에 추가하고
    else:
        numbers.pop() #0이면 뒤 요소에서 뺴준다

    if len(numbers) == 0:
        numbers.append(0) #리스트가 비었으면 0을 추가해준다.
print(sum(numbers))
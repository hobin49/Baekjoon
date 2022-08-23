#입력 값을 받아준다.
N, K = map(int, input().split())

#빈 리스트를 만들고
lst = []

#1~N까지의 수를 담은 리스트를 만든다.
num = [i+1 for i in range(N)]

#숫자를 담을 변수
cnt = 0 

#N크기만큼 range를 돌려준다.
for i in range(N):
    #for 문을 다 돌떄까지 K-1을 cnt에 누적해준다.
    cnt += K -1 
    #만약 그 숫자가 수를 담은 리스트의 길이보다 크거나 같으면
    if cnt >= len(num):
        #cnt에 cnt를 num의 길이만큼 나눈 나머지를 할당해준다.
        cnt %= len(num)
    #빈 리스트에 그 값을 넣어준다.
    lst.append(str(num[cnt]))
    #해당 숫자를 리스트에서 pop해준다.
    num.pop(cnt)
#join을 활용해서 숫자를 더해준다. join함수를 사용해서 comma기준으로 join해준다.
print('<' + ", ".join(lst) + ">")    

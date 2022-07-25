n = int(input())

first = 0
second = 0
third = 0

one_num = 99 # 100 보다 작으면 총 개수가 99개이니 미리 변수에 담고

if n < 100:
    one_num = n
    
else:
    for i in range(100, n+1): #100 이상 부터는 각 자릿수 분해
        first = i // 100 
        second = i % 100 // 10
        third = i % 10

        if (first - second) == (second - third): # 1,2,3번째 자리가 같으면
            one_num += 1 # += 1

print(one_num)
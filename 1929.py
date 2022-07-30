import math 
A, B = map(int, input().split())
#처음엔 모ㄴ 소가 True인 것으로 초기화(0과 1은 제외)
array  = [True for i in range(B + 1)]

#에라토스테네스의 체 알고리즘 수행
#2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(B)) + 1):
    if array[i] == True: #i가 소수인 경우(남은 수의 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= B:
            array[i * j] = False
            j += 1


#모든 소수 출력
for i in range(A, B + 1):
    if array[i]:
        print(i, end=' ')


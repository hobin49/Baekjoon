T = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

temp = B

result = 0
A.sort() #오름차순 정렬
temp.sort(reverse=True) #내림차순 정렬


for index, (value1, value2) in enumerate(zip(A, temp)): # 두 리스트를 합치고 
    result += (value1 * value2) #각리스를 곱해서 result에 더해준다
print(result)
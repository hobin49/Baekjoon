
num_1, num_2 = input().split()


num_1 = int(num_1[::-1]) #문자열 슬라이싱을 이용해서 거꾸로 출력
num_2 = int(num_2[::-1])

print(max(num_1, num_2)) #max함수를 사용해서 둘 중에 더 큰 값을 출력


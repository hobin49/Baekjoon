#수도코드 초안
#4.중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
#5.연산 가능한 수의 조합을 만들어야한다(어떻게? 가능한 모든 조합을 구해야하니깐  permutataions? 써야하나...)
#6.문제에서 나눗셈은 정수 나눗셈으로 몫만 취한다 (c = a // b)
#7. 각 연산을 진행하고 계산한 값들을 담고 그리고 최댓값과 최솟갑을 구해야지 문제가 끝난다 
from itertools import permutations
#1.입력 값을 받아주고
N = int(input())
#2.주어진 연산자를 리스트로 받아줘야 연산이 가능하겠지?
number = list(map(int, input().split()))
#3.연산자의 개수
calculations = list(map(int, input().split()))
#연산자를 만들어줘?
calculator = ["+", "-", "*", "//"]

#4.곱셈, 나눗셈, 덧셈, 뺄셈 총 4번 진행을 해준다. 
# for i in range(len(calculator)):

#4.중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
minimum = -1e9
maximum = 1e9


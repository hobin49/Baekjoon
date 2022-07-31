import math
N, K = map(int, input().split())
print(math.comb(N, K)) #math 모듈의 comb함수는 본질적으로 이항 계수와 동일한 공식을 갖는 주어진 값의 조합을 반환한다.

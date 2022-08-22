import math
# 모듈 활용
print(math.factorial(int(input())))

# 다른 방법 팩토리얼 직접 구현
def factorial_for(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial_for(int(input())))

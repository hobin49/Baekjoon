# 가우스 문제
# 입력값을 받아주고
N, P, Q = map(int, input().split())

# 리스트를 이용하면 메모리 초과가 뜬다. 그래서 해시 문제니 딕셔너리를 활용했다.
dp = {}
dp[0] = 1

# 재귀 방식에서 아이디어 도출
def fibo(N):
    # N에 해당하는 값이 이미 dp에 있으면 그것을 출력해주고
    if N in dp:
        return dp[N]
    # 아니면 계산을 해준다.
    else:
        dp[N] = fibo(N // P) + fibo(N // Q)
        return dp[N]


print(fibo(N))


# N, P, Q = map(int, input().split())

# # 재귀 방식
# def fibo(N):
#     if N == 0:
#         return 1
#     else:
#         return fibo(N // P) + fibo(N // Q)


# print(fibo(N))


# import sys

# sys.setrecursionlimit(10**9)
# dp = [0] * 10000001
# dp[0] = 1

# N, P, Q = map(int, input().split())

# for i in range(1, N + 1):
#     dp[i] = dp[i // P] + dp[i // Q]

# print(dp[N])


# N, P, Q = map(int, input().split())

# dp = {}
# dp[0] = 1

# # 재귀 방식
# def fibo(N):
#     if dp[N] != 0:
#         return dp[N]
#     else:
#         dp[N] = fibo(N // P) + fibo(N // Q)
#         return dp[N]


# print(fibo(N))

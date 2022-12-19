# 입력값 받아주기
n = int(input())

m = []
for _ in range(n):
    m.append(int(input()))

# 정렬해준다 내림차순으로
m.sort(reverse=True)

# 이제 for문을 돌면서 결과값을 담아준다.
result = []
for i in range(n):
    # 무게가 적을수록 더 많은 로프를 들 수 있다.
    result.append(m[i] * (i + 1))

print(max(result))

# n = int(input())
# m = []

# for i in range(n):
#     m.append(int(input()))

# m.sort(reverse=True)
# result = []

# for j in range(n):
#     result.append(m[j] * (j + 1))

# print(result)

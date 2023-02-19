n, k = map(int, input().split())

numbers = list(map(int, input().split()))

result = -100 * k
total = 0
for j in range(k):
    total += numbers[j]

if total > result:
    result = total

p = []
for i in range(0, n-k):
    total -= numbers[i]
    print(total)
    total += numbers[i+k]
    p.append(total)

print(p)
# print(new, new1)
# result = []
# for i, v in zip(new, new1):
#     result.append(i + v)

# print(max(result))
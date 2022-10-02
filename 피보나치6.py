s = [0, 1, 1]
n = int(input())
for i in range(3, n + 1):
    s.append(s[i - 1] + s[i - 2])
print(s[n])

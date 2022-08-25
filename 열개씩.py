s = 'BaekjoonOnlineJudge'
result = s[0:10]
k = 10
output = [s[i:i + 10] for i in range(0, len(s), 10)]
print(*output, sep ="\n")
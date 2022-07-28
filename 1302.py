from collections import Counter
result = []

for i in range(int(input())):
    book = input()
    result.append(book)

cnt = Counter(sorted(result))
print(cnt.most_common()[0][0])
x_ = []
y_ = []
for _ in range(3):
    k, n = map(int, input().split())
    x_.append(k)
    y_.append(n)

for i in range(3):
    if x_.count(x_[i]) == 1:
        x = x_[i]
    if y_.count(y_[i]) == 1:
        y = y_[i]
print(x, y)

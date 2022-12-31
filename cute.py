t = int(input())
number = []
for _ in range(t):
    number.append(int(input()))

zero = 0
one = 0

for i in number:
    if i == 0:
        zero += 1
    else:
        one += 1

if zero > one:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

n = int(input())
alpha = input()

num = []
for _ in range(n):
    num.append(int(input()))

stack = []

for i in alpha:
    if "A" <= i <= "Z":
        stack.append(num[ord(i) - ord("A")])
    else:
        first = stack.pop()
        second = stack.pop()
        # 앞의 피연산자들을 뒤부터 계산하는 방식
        if i == "-":
            stack.append(second - first)
        elif i == "/":
            stack.append(second / first)
        elif i == "*":
            stack.append(first * second)
        elif i == "+":
            stack.append(second + first)

print("%.2f" % stack[0])

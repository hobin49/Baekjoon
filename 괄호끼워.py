bracket = list(map(str, input()))
cnt = 0
stack = []
for b in bracket:
    if b == "(":
        stack.append(b)
    else:
        if len(stack) == 0:
            cnt += 1
        else:
            stack.pop()
    print(stack)
if len(stack) != 0:
    cnt += len(stack)
print(cnt)

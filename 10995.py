n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('* ' * n) # n의 수만큼 곱해준다
    else:
        print(' *' * n)
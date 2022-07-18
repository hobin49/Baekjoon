while 1: # while 0이면 False, 1이면 True
    a, b = map(int, input().split())
    if (a == 0 and b == 0): # a랑 b가 0이면 끝 
        break 
    else:
        print(a + b) # 0이 아니면 더하기
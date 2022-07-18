while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError: #EOF를 이용하면 입력이 끝날 때까지 계속 데이터를 받아올 수 있다.
        break

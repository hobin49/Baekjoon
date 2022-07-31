while True: #0이 아니라면
    A = input()

    if A == '0': #입력값이 0이면 break
        break

    if A == A[::-1]: #거꾸로 뒤집은거랑 비슷하면
        print('yes')
    else:
        print('no')  #아니면 False


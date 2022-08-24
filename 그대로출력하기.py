#try except구문을 활용해서 만약에 입력값이 있으면 계속 입력을 받고 없으면 종료한다.
while True:
    try:
        a = input()
        print(a)
    except:
        break

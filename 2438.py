A = int(input())

for i in range(1, A+1):
    for j in range(i):
        print("*", end='') #end를 사용하면 그 뒤의 출력값과 이어서 출력한다. 즉 줄바꿈을 하지 않게 된다.

    print()
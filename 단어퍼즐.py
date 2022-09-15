
i = 1
#테스트 케이스가 없을때는 while문을 사용한다
while True:
    a = input()
    b = input()
    #end 발견시 종료
    if a == "END" and b == "END":
        break
    #end가 아니면 정렬해주고 같은지 다른지 확인
    else:
        A = ''.join(sorted(a))
        B = ''.join(sorted(b))
        if A == B:
            print("Case", str(i)+ ": same")
        elif A != B:
            print("Case", str(i)+ ": different")
            
        i += 1	# 반복문 한 번씩 돌 때마다 1씩 늘어

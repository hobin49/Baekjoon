#입력값을 받아준다
n = int(input())

#짝수인지 홀수인지 파악할 변수와
line = 0
#라인의 마지막 인덱스를 담을 변수
end = 0
#n이 2라면 line = 2 end = 3 diff = 1
#n이 3라면 line = 2 end = 3 diff = 0
#입력값이 0보다 크면 홀짝 담은 변수에 1씩 계속 증가하고 마지막 인덱스를 담을 변수에 누적시킨다.
while n > end:
    line += 1
    end += line 

#마지막 인덱스에서 입력값을 받은 값을 빼준값을 변수에 담아 놓고
diff = end - n
#만약 짝수면 분자가 1씩 증가 분모가 감소한다.
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1

#만약 홀수면 분자가 감소하고 분모가 증가한다
else:
    top = diff + 1
    bottom = line - diff

print(f"{top}/{bottom}")
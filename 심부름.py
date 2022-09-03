m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
total = m1 + m2 + m3 + m4
seconds = total % 60
minute = int(total / 60)

print(minute, seconds, sep="\n")
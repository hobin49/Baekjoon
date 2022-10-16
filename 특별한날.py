n = int(input())
m = int(input())

if n == 1:
    print("Before")

elif n >= 3:
    print("After")

else:
    if m < 18:
        print("Before")
    elif m == 18:
        print("Special")
    else:
        print("After")

while True:
    triangle = sorted(list(map(int, (input().split()))))
    if  triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
        
    if pow(triangle[0], 2) + pow(triangle[1], 2) == pow(triangle[2], 2):
        print("right")
    else:
        print("wrong")

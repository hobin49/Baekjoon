for _ in range(3):
    n = list(map(int, input().split()))
    result = n.count(0)
    if result == 0:
        print("E")
    elif result == 1:
        print("A")
    elif result == 2:
        print("B")
    elif result == 3:
        print("C")
    elif result == 4:
        print("D")

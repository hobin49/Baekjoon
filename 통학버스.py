n, k, s = map(int, input().split())


left = []
right = []
for _ in range(n):
    location, numbers = map(int, input().split())
    if location < s:
        left.append([s - location, numbers])
    else:
        right.append([abs(s - location), numbers])

left.sort()
right.sort()


def bus(a: list):
    total_distance = 0
    while a:
        total_distance += a[-1][0]
        capacity = k
        while capacity and a:
            if a[-1][1] > capacity:
                a[-1][1] -= capacity
                capacity = 0
            else:
                capacity -= a[-1][1]
                a.pop()

    return total_distance * 2


print(bus(left) + bus(right))

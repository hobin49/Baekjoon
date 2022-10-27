t = int(input())
for _ in range(t):
    lst = []
    dictionary = {}
    n = int(input())
    for _ in range(n):
        number = input()
        lst.append(number)
    for num_ in lst:
        dictionary[num_] = dictionary.get(num_, 0) + 1

    for num1 in lst:
        search = ""
        flag = True
        for p in num1:
            search += p
            if search in dictionary.keys() and search != num1:
                flag = False

    if flag == False:
        print("NO")
    else:
        print("YES")

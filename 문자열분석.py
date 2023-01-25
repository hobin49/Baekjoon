while True:
    try:
        answer = [0] * 4
        n = input()
        for i in range(len(n)):
            if n[i].islower():
                answer[0] += 1

            elif n[i].isupper():
                answer[1] += 1

            elif n[i].isdigit():
                answer[2] += 1

            elif n[i].isspace():
                answer[3] += 1
        print(" ".join(map(str, answer)))
    except:
        break

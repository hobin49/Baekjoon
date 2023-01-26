import sys

input = sys.stdin.readline
n, k = map(int, input().split())
answers = []


def back(number, answer):
    if number == n:
        answers.append(answer)
        return

    if number + 1 <= n:
        back(number + 1, answer + [1])

    if number + 2 <= n:
        back(number + 2, answer + [2])

    if number + 3 <= n:
        back(number + 3, answer + [3])


back(0, [])


if len(answers) < k:
    print(-1)
else:
    answers.sort()
    answer = answers[k - 1]
    print(*answer, sep="+")

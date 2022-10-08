# 방법 1
# import sys

# input = sys.stdin.readline
# N, K = map(int, input().split())
# # 최대한 비용을 아끼려면 오름차순 정렬을 해서 묶어줘야 한다.
# students = sorted(list(map(int, input().split())))

# # 인접한 유치원생들의 키 차이를 구하기 위해
# diffrence = []

# for i in range(len(students) - 1):
#     diffrence.append(students[i + 1] - students[i])

# # 내림차순 정렬(티셔츠 만드는 비용의 합을 최소화 하고 싶으면 비용 많이 드는 것을 제외해야 한다.)
# diffrence = sorted(diffrence, reverse=True)

# # 최소비용에 해당하지 않는 애들을 총 길이에서 빼준다.
# print(sum(diffrence[K - 1 :]))

# 방법 2
import sys

input = sys.stdin.readline


def tshirt():
    N, K = map(int, input().split())
    # 최대한 비용을 아끼려면 오름차순 정렬을 해서 묶어줘야 한다.
    students = sorted(list(map(int, input().split())))

    # 총길이
    length = students[-1] - students[0]

    # 인접한 유치원생드르이 키 차이를 구해서 리스트에 담아준다.
    for i in range(len(students) - 1):
        diffrence.append(students[i + 1] - students[i])

    # 내림차순 정렬(티셔츠 만드는 비용의 합을 최소화 하고 싶으면 비용 많이 드는 것을 제외해야 한다.)
    diffrence = sorted(diffrence, reverse=True)

    # 최소비용에 해당하지 않는 애들을 총 길이에서 빼준다.
    return length - sum(sorted(diffrence[: K - 1]))


print(tshirt())

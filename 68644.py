# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    arr = []
    answer = []
    numbers = list(combinations(numbers, 2)) # combinations 활용해서 2개씩 묶어 줬고
    for num in numbers:
        arr.append(sum(num)) # 합을 arr라는 리스트에 담아주고
        
    for i in arr: #arr를 돌면서
        if i not in answer: #중복된 결과값을 제거하기 위해서 arr의 요소 중에서 answer에 없으면
            answer.append(i) # 추가해준다
            answer.sort() # 오름차순으로 정렬해준다
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

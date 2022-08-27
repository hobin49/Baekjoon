from collections import deque
def solution(queue1, queue2):
    #앞에 요소를 빼기 위해 큐보다는 빠른 덱을 사용해줬다.
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    #queue1
    sum_q1 = sum(queue1)
    # 각각 리스트의 합은 서로 같아야 하므로 두 개의 리스트를 더한 값을 2로 나눈 값을 할당해준다.
    div = (sum(queue1) + sum(queue2)) // 2
    #이동할 때마다 카운트 해줄 변수
    
    cnt = 0
    #리스트가 빌때까지 돌아주면서
    while len(queue1) != 0 and len(queue2) != 0:
        #두 개 중에서 하나의 리스트만 균형을 맞춰주면 다른 한 쪽도 자동으로 균형이 맞춰진다 그래서 큐1만 활용한다. 
        #만약 큐1의 합이 전체 큐를 2로 나눈 값보다 크다면 이동을 해야한다.
        if sum_q1 > div:
            #문제에서 요구하는 것처럼 큐1의 맨 왼쪽 요소를 빼주고
            cur = queue1.popleft()
            #큐1의 총 합계에서 빼준 값을 빼주고
            sum_q1 -= cur
            #count += 1을 해준다.
            cnt += 1
        #만약 큐1의 합이 전체 큐를 2로 나눈 값보다 작다면 큐2리스트에서 값을 빼서 보충 받아야 한다.
        elif sum_q1 < div:
            # 큐2에서 맨 앞의 요소를 빼주고
            cur2 = queue2.popleft()
            # 큐1에 그 값을 맞춰준다.
            queue1.append(cur2)
            #큐1 합계에 빼준 요소를 넣어줘서 값을 맞춰주는 시도를 한다.
            sum_q1 += cur2
            #count += 1 해준다.
            cnt += 1
        #만약에 큐1의 값이 전체 큐를 2로 나눈 값과 일치하면 count 해준 것을 return해준다.
        else:
            return cnt
    #어떤 방법을 쓰더라도 각 큐의 원소 합을 같게 만들 수 없으므로 -1을 return해준다.
    return -1
    
#     div = (sum(queue1) + sum(queue2)) //2 
#     cnt = list()
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     sum_queue = queue1 + queue2
#     comb_list = []
#     for n in range(len(sum_queue) + 1):
#         cnt += list(combinations(sum_queue, n))

#     for i in cnt:
#         comb = sum(list(i))
#         comb_list.append(comb)
    
#     if div not in comb_list:
#         return -1
    
#     answer = 0
    
#     while sum(queue1) != div and sum(queue2) != div:
#         if sum(queue1) == sum(queue2):
#             break
#         if sum(queue1) < sum(queue2):
#             cur = queue2.popleft()
#             queue1.append(cur)
#             answer += 1
#         else:
#             cur2 = queue1.popleft()
#             queue2.append(cur2)
#             answer += 1
#     return answer
        
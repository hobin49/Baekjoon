
# n = int(input())
# for i in range(n):
#     ps = input()
#     while '()' in ps: #while문을 활용해서 b에 입고 닫고가 있다면
#         ps = ps.replace('()', '') # replace 함수를 사용해서 "()" -> 이거를 빈 곳으로 만들어준다. 
    
#     print("NO" if ps else "YES") #if b에 어떠한 요소가 있다면 No 아니면 yes 



#다른 풀이 
# T = int(input())

# for _ in range(T):
#     stack = list(input())
#     ps_check = 0

#     for i in stack:
#         if i == "(": # 여는 괄호면 1을 더해주고
#             ps_check += 1
        
#         elif i == ")": #닫는 괄호면 1을 닫고
#             ps_check -= 1 

#         if ps_check < 0: #닫는 괄호가 먼저 나오면 안 된다
#             print("NO")
#             break

#     if ps_check > 0: # pair_check가 여는 괄호 "("가 더 많으므로 No
#         print("NO")
#     elif ps_check == 0:  #"#비어있다면 Yes"
#         print("YES")


# T = int(input())

# for i in range(T):
#     stack = []
#     a = int(input())
#     for j in a:
#         if j == "(":
#             stack.append(j)
#             print(stack)
#         elif j == ")":
#             if len(stack):
#                 stack.pop()
#             else: #스택이 비었으면 "("가 없어 짝이 안 맞는다.
#                 print("NO")
#                 break
#     else: #break문으로 끊기지 않고 수행됐을 경우 수행한다.
#         if not stack: # break문으로 안 끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#             print("YES")
#         else: #break안 걸렸더라도 스택에 괄호가 들어있다면 NO다. 
#             print("NO")


T = int(input())

# 열린괄호, 닫힌괄호를 미리 변수에 설정해준다.
LEFT = "("
RIGHT = ")"
for i in range(T):
    #빈 리스트 2개 만들고
    left_stack = []
    right_stack = []
    a = input()
    #열린괄호라면 left_stack에 추가
    if a == LEFT:
        left_stack.append(a)
        print(left_stack)
    #닫힌괄호라면 1.left_stack에 요소가 있다면 pop을 해주고 아니면 right_stack에 넣어준다
    if a == RIGHT:
        if len(left_stack) != 0:
            left_stack.pop()
        else:
            right_stack.append(a)
#leftstack 이나 rightstack 둘 다 0이라면 yes출력 아니면 No를 출력
if len(left_stack) == 0 and len(right_stack) == 0:
    print("Yes")
else:
    print("No")
first = list(input())
second = list(input())

result = []

#첫 번째 리스트에서 2번째 리스트에서 중복되는 요소 체크후에 리스트에 넣어주고 두번째 리스트에서 제거한다
for element in first:
    if element in second:
        result.append(element)
        second.remove(element)

#첫 번째 리스트에서 중복된 요소가 첫번째 리스트에 있으면 제거해주고
for r in result:
    if r in first:
        first.remove(r)

#중복되지 않는 요소의 길이를 더해준다.
print(len(first)+len(second))
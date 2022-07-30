N = 0
sum_ = 0
numbers = [] * 10001
for i in range(1, 10001):
    numbers.append(i) #1부터 10000까지 수를 리스트에 담기

for i in range(1, 10001):
    num = [(int(k)) for k in str(i)] #각 자릿수를 분해한 값
    sum_ = i + sum(num) # 어떤 값은 = 어떤 수와 + 어떤 수의 자릿수를 분해해서 합한 값과 같다
    if sum_ in numbers: #아까 만들어 놓은 number
        numbers.remove(sum_)
print(*numbers, sep = "\n")




m = [] #길이를 닮을 리스트
temp = [] 
for i in range(5):
    A = input()
    temp.append(A)
    m.append(len(A))
    
    
for i in range(max(m)):
     for j in range(0, 5):
        if i < m[j]:
            print(temp[j][i], end = "")
        
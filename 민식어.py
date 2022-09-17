t = int(input())
#먼저 민식어의 알파벳과 번호를 부여
minsik = {'a':1, 'b':2, 'k': 3, 'd':4, 'e':5, 'g':6, 'h':7, 'i':8, 'l':9, 'm':10 ,'n':11, 'z':12, 'o':13, 'p':14, 'r':15, 's':16, 't':17, 'u':18, 'w':19, 'y':20}
#해당 알파벳과 순서를 받기 위한 리스트
alphabet = []
for _ in range(t):
     #알파벳을 서로 분리해주고
     word = input()
     #예제 출력 2번 부분에서 밑에 주석 부분을 해결하기 위해 ng를 민식어에서 사용하지 않는 알파벳으로 z로 바꿨다.
     #('alab', [1, 9, 1, 2]), ('alak', [1, 9, 1, 3]), ('alam', [1, 9, 1, 10]), ('ang', [1, 11, 6]), ('anim', [1, 11, 8, 10]), ('ano', [1, 11, 13])]
     # => [('alab', [1, 9, 1, 2]), ('alak', [1, 9, 1, 3]), ('alam', [1, 9, 1, 10]), ('anim', [1, 11, 8, 10]), ('ano', [1, 11, 13]), ('ang', [1, 12])]
     replace_ = word.replace('ng', 'z')
     #알파벳에 해당하는 순서를 받기 위한 리스트 
     answer = []
     #알파벳을 돌면서
     for alpha in replace_:
          #알파벳이 민식어에 있으면 
          if alpha in minsik.keys():
               #알파벳에 해당하는 순서를 리스트에 담아준다.
               answer.append(minsik[alpha])
     #(단어, 알파벳 순서)를 담아주고          
     alphabet.append((word,answer))
     #알파벳 순서를 기준으로 정렬해준다.
     alphabet = sorted(alphabet, key=lambda x: x[1])

#최종값을 출력
for a in alphabet:
     print(a[0])
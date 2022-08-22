#소문자를 만들기 위한 모듈 import
from string import ascii_lowercase

#딕셔너리 만들고
alphabet_dict = {}
#입력값 받고
S = input()

#알파벳리스트를 딕셔너리에 넣어준다
for i in ascii_lowercase:
    alphabet_dict[i] = -1

#딕셔너리를 돌면서
for k in S:
    #만약 해당 문자열이 있으면
    if k in alphabet_dict:
        #딕셔너리 value에 문자열의 해당 인덱스를 넣어준다.
        alphabet_dict[k] = S.index(k)
#언팩킹해서 print
print(*alphabet_dict.values())


#다른 사람 풀이
word = input()
#아스키코드 숫자 범위
alphabet = list(range(97, 123))

#해당 숫자를 문자열로 변환해주고 index로 접근
for x in alphabet:
    print(word.find(chr(x)))
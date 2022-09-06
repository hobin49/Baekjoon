vowel = ['a', 'e', 'i', 'o', 'u']

alpha = input()
cnt = 0

for i in alpha:
    if i in vowel:
        cnt += 1
    
print(cnt)
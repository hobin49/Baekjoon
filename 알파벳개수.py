from string import ascii_lowercase

dictionary = {}

s = input()

for i in ascii_lowercase:
    dictionary[i] = 0

for k in s:
    if k in dictionary:
        dictionary[k] += 1

print(*dictionary.values())
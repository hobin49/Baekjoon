button = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
n = input()
m = int(input())
broken = input().split()


for i in broken:
    if i in button:
        button.remove(i)
print(button)
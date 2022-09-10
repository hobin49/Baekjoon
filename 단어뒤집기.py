a = input().split()
result = []
tag_left = "<"
tag_right = ">"
for i in a:
    if tag_left in i and tag_right in i:
        t1 = i.index(tag_left)
        t2 = i.index(tag_right)
        a.remove(i[t1:t2])


print(a)

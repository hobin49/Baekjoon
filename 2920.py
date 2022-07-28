note = list(map(int, input().split()))

if sorted(note) == note: #sorted 해서 오름 차순이면 오름차순
    print("ascending")

elif sorted(note, reverse=True) == note: #sorted 내림차순이면 내림차순
    print("descending")

else:
    print("mixed") #둘 다 아니면 mixed
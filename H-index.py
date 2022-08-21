def solution(citations):
    #인용횟수가 논문수보다 크거나 같으면 넣을 리스트
    H_index = []
    #인용횟수가 논문수보다 작으면 넣을 리스트
    No_H_index = []
    #논문수와 인용횟수를 비교하기 위해서 인용횟수를 내림차순으로 정렬한다.
    ci_sorted = sorted(citations, reverse = True)
    #논문수와 인용횟수를 비교하기 위해서 enumerate를 활용해서 인덱스를 논문수로 활용하겠어 논문수는 1부터 시작하니 1부터 시작해준다.
    for a, c in enumerate(ci_sorted, start = 1):
        # 만약 인용횟수가 논문수보다 크거나 같으면 H-index 리스트에 넣어준다
        if c >= a:
            H_index.append(c)
        #만약 인용횟수가 논문수보다 작다면 반대편 리스트에 넣어준다.
        else:
            No_H_index.append(c)
    #해당 길이를 출력하는 것이 h-index를 출력하는 것과 같다.        
    return len(H_index)
        
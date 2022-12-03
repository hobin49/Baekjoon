def solution(survey, choices):
    answer = ""
    # 각 성격 유형의 점수를 계산하기 위해서 딕셔너리에 담아준다.
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # len(survey) == len(choices) 둘 중 하나 선택해서 해당 길이만큼 돌아준다.
    for i in range(len(choices)):
        # survey의 두개의 유형이 붙어있으니까 strip을 사용해서 떨어뜨린다.
        a, b = survey[i].strip()
        # 만약 해당 선택점수가 4점 미만이라면
        if choices[i] < 4:
            # 앞의 유형에 4 - 선택점수
            scores[a] += 4 - choices[i]
        # 만약 해당 선택점수가 4점이 넘는다면
        elif choices[i] > 4:
            # 뒤의 유형에 선택점수 - 4
            scores[b] += choices[i] - 4

    # 만약 T가 R보다 크다면 T유형을 answer에 더해주고
    if scores["R"] < scores["T"]:
        answer += "T"
    # 작거나 같으면 사전적으로 R이 먼저이므로 R을 더해준다.
    else:
        answer += "R"

    if scores["C"] < scores["F"]:
        answer += "F"
    else:
        answer += "C"

    if scores["J"] < scores["M"]:
        answer += "M"
    else:
        answer += "J"

    if scores["A"] < scores["N"]:
        answer += "N"
    else:
        answer += "A"

    return answer

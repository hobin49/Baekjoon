def solution(phone_book):
    #빈 딕셔너리를 만들고
    dictionary  = {}
    answer = True
    #딕셔너리로 만들어준다.
    for number in phone_book:
        dictionary[number] = dictionary.get(number, 0) + 1

    # 숫자를 꺼내자~
    for num in phone_book:
        #숫자를 담을 변수!
        search = ""
        #숫자를 뜯어보자~
        for n in num:
            #뜯은 숫자를 담아보자~
            search += n
            #숫자가 dict의 key에 값에 있고 전체 숫자랑은 달라야해 알았징?
            if search in dictionary.keys() and search != num:
                # 그래야 False니까!!!
                answer = False
    #그게 아니면 True            
    return answer
def solution(n):
    binary_n = bin(n).lstrip("0b")
    cnt = 0
    max_cnt = 0
    for i in binary_n:
        if i == "1":
            if max_cnt < cnt:
                max_cnt = cnt
                cnt = 0
            else:
                cnt = 0
        else:
            cnt += 1
    return max_cnt

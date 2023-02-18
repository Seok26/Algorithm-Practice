def solution(s):
    answer = [0, 0]

    while True:
        #0. Break
        if s == '1':
            break

        #1. 0 제거
        answer[1] += s.count('0')
        s = s.replace("0", "")


        #2. 길이 c를 구한 후 c를 2진법으로 표현
        length = len(s)
        s = bin(length)[2:]
        answer[0] += 1

    return answer


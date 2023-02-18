def solution(n):
    answer = 0
    condition2 = bin(n)[2:].count('1')
    append_number = 1
    while True:
        #조건 1
        answer = n + append_number

        #조건 2
        check_condition2 = bin(answer)[2:].count('1')

        #조건 3. -> 탈출
        if check_condition2 == condition2:
            break
        append_number += 1

    return answer
def solution(n, words):
    answer = [0, 0]

    process = [] # 단어의 진행 상황
    process_turn = {} # 참가자별 턴 회수
    turn = 1 #1번부터 시작

    for i in range(1, n + 1):
        process_turn[i] = 0

    for word in words:
        #0. process 초기화
        if len(process) == 0:
            process.append(word)
            process_turn[turn] += 1
            turn += 1
            continue

        #1. 끝말잇기 여부 체크
        before = process[-1][-1]
        after = word[0]
        if before != after:
            process_turn[turn] += 1
            answer[0] = turn
            answer[1] = process_turn[turn]
            break
        #끝말잇기 충족 후 이미 나왔던 단어 확인
        else:
            if word in process:
                process_turn[turn] += 1
                answer[0] = turn
                answer[1] = process_turn[turn]
                break

            #끝말잇기 + 첫 등장 단어
            else:
                process.append(word)
                process_turn[turn] += 1
                turn += 1
                if turn > n:
                    turn = 1

    return answer
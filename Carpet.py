def solution(brown, yellow):
    answer = []
    process = [] #(가로, 세로) 경우의 수
    value = brown + yellow #카펫의 개수

    for i in range(3, value):
        if value % i == 0 and (i >= (value / i)):
            process.append((i, value // i))

    for pro in process:
        row = pro[0]
        col = pro[1]
        array = [[1] * col for _ in range(row)] #브라운 0 노랑 1
        check = 0

        #Brown 처리
        #상하
        for i in range(col):
            array[0][i] = 0
            array[-1][i] = 0
        #좌우
        for i in range(row):
            array[i][0] = 0
            array[i][-1] = 0

        for arr in array:
            check += arr.count(1)

        if check == yellow:
            return pro
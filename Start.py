#Progrmmers Lever 2. JadenCase
def solution(s):
    #시작 시 모든 문자열은 소문자로 변경
    s = s.lower()
    li = list(s)

    for i in range(len(li)):
        #공백이면 건너뛰기
        if li[i] == " ":
            continue

        #소문자인 경우
        if ord('a') <= ord(li[i]) <= ord('z'):

            #JadenCase
            if li[i - 1] == " " or i == 0:
                li[i] = li[i].upper()


    return ''.join(s for s in li)
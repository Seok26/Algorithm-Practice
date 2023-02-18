def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            before = stack[-1]
            if before == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False

    
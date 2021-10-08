# 짝지어 제거하기
# 괄호 문제와 유사, 스택을 이용
def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    s = list(s)
    stack = [s[0]]
    for char in s[1:]:
        if not stack:
            stack.append(char)
            continue
        val = stack.pop()
        if val != char:
            stack.append(val)
            stack.append(char)
    if stack:
        return 0
    else:
        return 1


s = "abbcdaadca"
print(solution(s))
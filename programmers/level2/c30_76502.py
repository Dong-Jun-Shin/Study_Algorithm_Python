# 괄호 회전하기
def is_right(s):
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if stack:
                val = stack.pop()
                if not char == bracket_dict[val]:
                    return False
            else:
                return False
    return not stack


def solution(s):
    answer = 0
    leng = len(s)
    s *= 2
    for i in range(leng):
        if is_right(s[i:i + leng]):
            answer += 1
    return answer

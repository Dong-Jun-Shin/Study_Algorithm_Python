# 괄호 변환
def reverse_str(u):
    temp = ""
    for char in u[1:-1]:
        if char == '(':
            temp += ')'
        else:
            temp += '('
    return temp

def get_idx(p):
    count = 0
    i = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            break
    return (i + 1)

def is_pair(u):
    pair = 0
    for char in u:
        if char == '(':
            pair += 1
        else:
            pair -= 1
        if pair < 0:
            return False
    return True

def solution(p):
    if is_pair(p):
        return p

    if len(p) == 0:
        return ""
    idx = get_idx(p)

    u = p[:idx]
    v = p[idx:]
    v = solution(v)

    answer = ""    
    if is_pair(u):
        answer = u + v
    else:
        answer = "("
        answer += v
        answer += ")"
        answer += reverse_str(u)
    return answer

p = "()))((()"
print(solution(p))

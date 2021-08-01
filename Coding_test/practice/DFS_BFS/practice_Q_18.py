# 괄호 변환

def get_balence_idx(_p):
    balence_cnt = 0
    for i in range(len(_p)):
        if _p[i] == "(":
            balence_cnt += 1
        else:
            balence_cnt -= 1

        if balence_cnt == 0:
            break
    return i

def proper_check(_u):
    balence_cnt = 0
    for char in _u:
        if balence_cnt < 0:
            return False
        if char == "(":
            balence_cnt += 1
        else:
            balence_cnt -= 1
    return True

def change_brackets(_u):
    temp = ""
    for char in _u:
        if char == "(":
            temp += ")"
        else:
            temp += "("
    return temp

def divide(_p):
    if _p == '':
        return ''
    if proper_check(_p):
        return _p

    u, v = "", ""
    result = ""
    
    idx = get_balence_idx(_p)
    u = _p[:idx + 1]
    v = _p[idx + 1:]

    if proper_check(u):
        return (u + divide(v))
    else:
        v_str = divide(v)
        result += "("
        result += '' if v_str is None else v_str
        result += ")"
        result += change_brackets(u[1:-1])
        return result

def solution(p):
    answer = ''    
    answer = divide(p)
    return answer


p = "()))((()"
print(solution(p))
# 괄호 변환
def check_right(u):
    count = 0
    for char in u:
        if char == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


def get_balence_idx(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            break
    return i + 1


def dfs(p):
    if len(p) <= 0:
        return p

    balence_idx = get_balence_idx(p)
    u = p[:balence_idx]
    v = p[balence_idx:]
    new_u = ""
    if check_right(u):
        return u + dfs(v)
    else:
        new_u = "(" + dfs(v) + ")"
        for char in u[1:-1]:
            if char == "(":
                new_u += ")"
            else:
                new_u += "("
    return new_u


def solution(p):
    answer = dfs(p)
    return answer


p = "(()())()"
print(solution(p))

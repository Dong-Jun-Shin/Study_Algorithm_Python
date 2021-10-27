# 이중우선순위큐
import bisect


def solution(operations):
    answer = []
    for oper in operations:
        oper = oper.split()
        if oper[0] == "I":
            bisect.insort_right(answer, int(oper[1]))
        elif oper[0] == "D":
            if answer:
                answer.pop() if oper[1] == "1" else answer.pop(0)
    answer = [answer[-1], answer[0]] if answer else [0, 0]
    return answer


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

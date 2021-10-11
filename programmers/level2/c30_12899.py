# 124 나라의 숫자
# 3진법 계산과 유사, 단 3진법에서 자리올림 하는 것을 4로 표현
# 4로 표현할 때 자리올림이 되면 안되기 때문에 몫(1몫=3의 크기)를 하나 가져와서,
#   나머지에 4가 존재하도록 처리

def get_scale_num(n):
    string = ''
    while n > 3:
        if n % 3 == 0:
            string += str(3)
            n = n // 3 - 1
        else:
            string += str(n % 3)
            n = n // 3
    string += str(n)
    return string[::-1]


def solution(n):
    answer = ''
    if n > 3:
        answer = get_scale_num(n)
    else:
        answer = str(n)
    answer = answer.replace('3', '4')
    return answer


n = 145
print(solution(n))

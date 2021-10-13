# 예상 대진표
# 2개가 한 그룹이 되는 점을 이용해서 binary를 이용
# 토너먼트의 루트와 2진법의 맨 앞자리는 같음
# 같은 뿌리에서 자릿수에 따라 나누어지며 값을 가짐
# 2진법을 순서대로 쓰고 자리올림 전까지 수는 앞자리가 같은 특성
# 팀은 1번부터지만, 2진법은 0부터 시작이므로 a, b에서 -1
# 각 수를 XOR(^) 연산하면 다른 위치가 경쟁을 하게 될 부분
# bit_length()로 2진법의 길이를 카운트
def solution(n, a, b):
    for i in range(11):
        print(bin(i)[2:].zfill(4))
    answer = (a - 1) ^ (b - 1)
    return answer.bit_length()


def solution(n, a, b):
    answer = 0
    while True:
        answer += 1
        a = a if a % 2 == 0 else a + 1
        b = b if b % 2 == 0 else b + 1
        if a == b:
            break
        a //= 2
        b //= 2
    return answer


n = 8
a = 4
b = 7
print(solution(n, a, b))

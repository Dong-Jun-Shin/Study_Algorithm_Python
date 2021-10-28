# N으로 표현
# DP를 활용하는 문제
# 0부터 경우의 수를 직접 종이에 확인하면서 접근
# 규칙을 파악해서 손 코딩 해보고, 코드 작성하기
def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        result = set([int(str(N) * i)])
        for j in range(i - 1):
            for num1 in dp[j]:
                for num2 in dp[-j-1]:
                    result.add(num1 + num2)
                    result.add(num1 - num2)
                    result.add(num1 * num2)
                    if num2 != 0:
                        result.add(num1 // num2)
        if number in result:
            return i
        dp.append(result)
    return answer

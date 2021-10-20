# 타겟 넘버
# 각 자리마다 들어갈 수 있는 경우의 수를 dfs로 모두 확인
def solution(numbers, target):
    answer = 0
    def dfs(num, depth):
        nonlocal answer
        if depth == len(numbers):
            if num == target:
                answer += 1
            return
        if depth == 1:
            for val in [-num, num]:
                dfs(val + numbers[depth], depth + 1)
                dfs(val - numbers[depth], depth + 1)
        else:
            dfs(num + numbers[depth], depth + 1)
            dfs(num - numbers[depth], depth + 1)
    dfs(numbers[0], 1)
    return answer



# 풀이 2
# 산술에 대한 순열은 비효율적
# 모든 수를 더한 경우에서 타겟을 뺀, 경우의 수를 구하면 타겟을 구한 경우와 같음
# (모든 수 - 타겟)으로 어떠한 수를 빼야 하는지 찾아야 하는데,
#    어떤 수던 이미 더했으니 빼는 연산까지 했을 때, 사용한 수는 두번씩 사용됨
#    사용한 수를 찾기 위해 2를 나누면 수를 더하는 조합만으로
#    (모든 수 - 타겟)을 구할 수 있음
# def dfs(numbers, target, idx, cnt):
#     # 재귀 호출되었을 때, 이미 더한 numbers 이후 원소를 위해 idx로 시작
#     for i in range(idx, len(numbers)):
#         # 반복문이 한번 돌았을 때, 다른 변수에 넣어 사용하지 않으면
#         #     현재 구해야할 target이 계속 처리되어 버림
#         temp = target
#         temp -= numbers[i]
#         if temp == 0:
#             cnt += 1
#         elif temp > 0:
#             # 지금까지 연산된 결과 temp와 i + 1부터 연산했을 때,
#             #     temp == 0인 경우를 반환해서 현재
#             cnt += dfs(numbers, temp, i + 1, 0)
#         elif temp < 0:
#             continue
#     return cnt    
            
            
# def solution(numbers, target):
#     answer = 0
#     new_target = (sum(numbers) - target) // 2
#     answer = dfs(numbers, new_target, 0, 0)
#     return answer
    

# numbers = [1, 3, 4, 1, 1]
# target = 3
# print(solution(numbers, target))

# 순위
# 플루이드 워셜을 이용한 풀이
def solution(n, results):
    answer = 0
    graph = [['?'] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 'Self'

    for s, e in results:
        graph[s-1][e-1] = 'Win'
        graph[e-1][s-1] = 'Lose'

    for i in range(n):
        for j in range(n):
            for k in range(n):
                # i가 k를 이겼고 k가 j를 이겼다면, i는 j를 이긴 것
                if graph[i][k] == graph[k][j] == 'Win':
                    graph[i][j] = 'Win'
                # i가 k에게 졌고, k가 j에게 졌다면, i는 j에게 진 것
                elif graph[i][k] == graph[k][j] == 'Lose':
                    graph[i][j] = 'Lose'

    # 0번 ~ n번 순위자에 대해 알 수 없는 순위가 있는지 확인
    for i in range(n):
        if '?' not in graph[i]:
            answer += 1
    return answer


# set을 이용한 풀이
# from collections import defaultdict


# def solution(n, results):
#     answer = 0
#     win_graph = defaultdict(set)    # 이긴 애들
#     lose_graph = defaultdict(set)   # 진 애들

#     # 결과에서 이기고 진 애들 그래프화
#     for winner, loser in results:
#         win_graph[loser].add(winner)
#         lose_graph[winner].add(loser)

#     for i in range(1, n+1):
#         # i한테 진 애들은 i를 이긴 애들한테도 진 것
#         for winner in win_graph[i]:
#             lose_graph[winner].update(lose_graph[i])
#         # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
#         for loser in lose_graph[i]:
#             win_graph[loser].update(win_graph[i])

#     for i in range(1, n+1):
#         # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
#         if len(win_graph[i]) + len(lose_graph[i]) == n-1:
#             answer += 1

#     return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# n = 8
# results = [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]]
print(solution(n, results))

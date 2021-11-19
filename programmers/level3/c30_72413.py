# 합승 택시 요금
# 모든 지점의 다익스트라를 구한 후, 모든 경유지점을 비교한 풀이
import heapq


def dijkstra(graph, s, n):
    dist = [int(1e9)] * (n + 1)
    dist[s] = 0
    q = [(s, 0)]
    while q:
        start, cost = heapq.heappop(q)
        if dist[start] < cost:
            continue
        for end, next_cost in graph[start]:
            if dist[end] > cost + next_cost:
                dist[end] = cost + next_cost
                heapq.heappush(q, (end, dist[end]))
    return dist
    
def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1
    graph = [[] for _ in range(n + 1)]
    min_list = []
    for start, end, cost in fares:
        graph[start - 1].append((end - 1, cost))
        graph[end - 1].append((start - 1, cost))
        
    for i in range(n):
        min_list.append(dijkstra(graph, i, n))

    answer = int(1e9)
    for i in range(n):
        answer = min(answer, min_list[s][i] + min_list[i][a] + min_list[i][b])
    return answer


# 플로이드 워셜로 작성한 코드(다익스트라보다 오래 걸림)
# def solution(n, s, a, b, fares):
#     answer = int(1e9)
#     graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
#     for i in range(n + 1):
#         graph[i][i] = 0

#     for start, end, cost in fares:
#         graph[start][end] = graph[end][start] = cost
    
#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
#     for i in range(1, n + 1):
#         if graph[s][i] == int(1e9) or graph[i][a] == int(1e9) or graph[i][b] == int(1e9):
#             continue
#         answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
#     return answer





print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

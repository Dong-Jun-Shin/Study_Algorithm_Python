# 배달
import heapq


def solution(N, road, K):
    answer = 0
    dist = [int(1e9)] * N
    graph = [[] for _ in range(N)]
    for a, b, cost in road:
        graph[a - 1].append((b - 1, cost))
        graph[b - 1].append((a - 1, cost))

    dist[0] = 0
    q = [(0, 0)]
    while q:
        start, now_dist = heapq.heappop(q)
        if now_dist > dist[start]:
            continue
        for end, cost in graph[start]:
            if dist[end] > now_dist + cost:
                dist[end] = now_dist + cost
                heapq.heappush(q, (end, dist[end]))
    answer = len([val for val in dist if val <= K])

    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
print(solution(N, road, K))

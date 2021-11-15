import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    # 크루스칼 알고리즘
    costs = [(c, s, e) for s, e, c in costs]
    heapq.heapify(costs)
    while costs:
        cost, s, e = heapq.heappop(costs)
        if find_parent(parent, s) == find_parent(parent, e):
            continue
        union_parent(parent, s, e)
        answer += cost
    return answer

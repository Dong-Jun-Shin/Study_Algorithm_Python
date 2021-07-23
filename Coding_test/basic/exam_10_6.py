# 부모 노드 찾는 함수
def find_parent(parent, e):
    if parent[e] != e:
        parent[e] = find_parent(parent, parent[e])
    return parent[e]


# 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 집의 개수N, 길의 개수M 받기
n, m = map(int, input().split())

# 부모 노드 테이블 초기화
parent = [i for i in range(n + 1)]

# 길의 정보 받기
graph = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

# 간선 정보를 비용에 따라 오름차순 정렬
graph.sort()

# 총 간선의 길이 비용
result = 0
# 신장 트리 분리를 위한 가장 비용이 큰 간선의 비용
last_cost = 0

# 모든 간선에 대해서, 사이클이 있는지 확인 후, 합치기
for val in graph:
    cost, a, b = val
    # 두 노드가 동일한 집합에 포함되어 있는지 확인(사이클 존재 여부)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last_cost = cost

print(result - last_cost)

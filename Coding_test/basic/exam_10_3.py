# find 정의
def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]


# union 정의
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드와 간선 개수 받기
v, e = map(int, input().split())
# 간선 리스트 받기
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 최소 신장 간선 테이블
minEdges = []
result = 0
# 부모 테이블 초기화
parent = [i for i in range(v + 1)]

# 간선 리스트 정렬
edges.sort()

# 최소 신장 트리 찾기
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        minEdges.append((cost, a, b))
        union_parent(parent, a, b)
        result += cost

print(result)
print(minEdges)

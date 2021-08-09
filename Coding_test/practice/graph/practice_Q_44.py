# 행성 터널(크루스칼, 여러개의 최소 신장 트리를 조합)
# N = 10만, 모든 간선의 개수는 N(N - 1)/2개, 모든 간선 약 50억개를 고려해야 함
# 터널의 비용은 x, y, z 각각 연산한 값중 최솟값이다. (각 좌표끼리 계산 및 정렬해도 최소 신장 트리가 됨)
# x, y, z 각각 트리의 간선이 될 수 있는 후보를 모아서, 최소 비용만으로 최소 신장 트리를 구성
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


n = int(input())
x_list = []
y_list = []
z_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
x_list.sort()
y_list.sort()
z_list.sort()

edges = []
for i in range(n - 1):
    edges.append((x_list[i + 1][0] - x_list[i][0], x_list[i][1], x_list[i + 1][1]))
    edges.append((y_list[i + 1][0] - y_list[i][0], y_list[i][1], y_list[i + 1][1]))
    edges.append((z_list[i + 1][0] - z_list[i][0], z_list[i][1], z_list[i + 1][1]))
edges.sort()

result = 0
parent = [i for i in range(n)]
for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)

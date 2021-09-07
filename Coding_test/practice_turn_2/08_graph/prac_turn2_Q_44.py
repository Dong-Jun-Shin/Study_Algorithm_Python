# 행성 터널
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
graph_x = []
graph_y = []
graph_z = []
for i in range(n):
    x, y, z = map(int, input().split())
    graph_x.append((x, i))
    graph_y.append((y, i))
    graph_z.append((z, i))

graph_x.sort()
graph_y.sort()
graph_z.sort()

edges = []
for i in range(n - 1):
    edges.append((graph_x[i + 1][0] - graph_x[i][0], graph_x[i + 1][1], graph_x[i][1]))
    edges.append((graph_y[i + 1][0] - graph_y[i][0], graph_y[i + 1][1], graph_y[i][1]))
    edges.append((graph_z[i + 1][0] - graph_z[i][0], graph_z[i + 1][1], graph_z[i][1]))

edges.sort()
parent = [i for i in range(n)]
result = 0
for cost, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)

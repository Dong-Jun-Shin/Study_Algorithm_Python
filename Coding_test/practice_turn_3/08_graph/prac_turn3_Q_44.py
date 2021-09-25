# 행성 터널
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a    


n = int(input())

x_list, y_list, z_list = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
x_list.sort()
y_list.sort()
z_list.sort()

edges = []
for i in range(1, n):
    x_val = x_list[i][0] - x_list[i - 1][0]
    y_val = y_list[i][0] - y_list[i - 1][0]
    z_val = z_list[i][0] - z_list[i - 1][0]
    edges.append((x_val, x_list[i][1], x_list[i - 1][1]))
    edges.append((y_val, y_list[i][1], y_list[i - 1][1]))
    edges.append((z_val, z_list[i][1], z_list[i - 1][1]))
edges.sort()

result = 0
parent = [i for i in range(n + 1)]
for cost, s_idx, e_idx in edges:
    if find_parent(parent, s_idx) == find_parent(parent, e_idx):
        continue
    union_parent(parent, s_idx, e_idx)
    result += cost

print(result)

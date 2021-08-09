# 어두운 길(크루스칼(최소 신장 트리))
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


n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    edges.append((z, x, y))

edges.sort()

idx = []
for i in range(len(edges)):
    z, x, y = edges[i]
    if find_parent(parent, x) == find_parent(parent, y):
        idx.append(i)
    union_parent(parent, x, y)

# 최소 신장 트리 만드는 과정 확인하고 
# 결과값 더해서 출력
result = 0
for i in idx:
    z, x, y = edges[i]
    result += z

print(result)

""" Test case
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""

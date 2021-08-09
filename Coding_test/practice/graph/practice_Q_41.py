# 여행 계획
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
parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    datas = list(map(int, input().split()))
    for j in range(n):
        if datas[j] == 1:
            union_parent(parent, i, j + 1)

m_list = list(map(int, input().split()))
prev_m_val = find_parent(parent, m_list[0])
for m_val in m_list[1:]:
    if prev_m_val != find_parent(parent, m_val):
        print("NO")
        break
else:
    print("YES")

""" Test case
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""

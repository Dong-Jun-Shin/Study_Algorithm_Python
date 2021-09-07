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
graph = []
for i in range(n):
    datas = list(map(int, input().split()))
    for j in range(len(datas)):
        if datas[j] == 1:
            union_parent(parent, i, j)

visit_plan = list(map(int, input().split()))
possible_bool = find_parent(parent, visit_plan[0])
for i in range(1, len(visit_plan) - 1):
    if possible_bool != find_parent(parent, visit_plan[i]):
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

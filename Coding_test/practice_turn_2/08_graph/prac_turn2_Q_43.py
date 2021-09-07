# 어두운 길
import sys


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


input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n)]
save_cost = 0
m_list = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    m_list.append((cost, x, y))
m_list.sort()

for cost, x, y in m_list:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        save_cost += cost

print(save_cost)

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

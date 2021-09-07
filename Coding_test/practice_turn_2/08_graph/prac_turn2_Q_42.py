# 탑승구
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a):
    a = find_parent(parent, a)
    if a > 0:
        parent[a] = a - 1


g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
p_list = []
for _ in range(p):
    p_list.append(int(input()))

for i in range(p):
    if find_parent(parent, p_list[i]) != 0:
        union_parent(parent, p_list[i])
    else:
        break

print(i)

""" Test case
4
3
4
1
1

4
6
2
2
3
3
4
4
"""

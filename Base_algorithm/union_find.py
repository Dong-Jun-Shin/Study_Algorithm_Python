def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a):
    a = find_parent(parent, a)
    b = a - 1
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


g = int(input())
p = int(input())
count = 0
parent = [i for i in range(g + 1)]
for _ in range(p):
    p_num = int(input())
    if find_parent(parent, p_num) == 0:
        break
    union_parent(parent, p_num)
    count += 1
    
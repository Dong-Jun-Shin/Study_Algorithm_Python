# 탑승구(서로소 집합)
# 가장 오른쪽부터 빈 곳을 찾아서 지정(큰 곳부터, 합집합 연산이 안될 때까지)
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


g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]

result = 0
for _ in range(p):
    p_val = find_parent(parent, int(input()))
    if p_val == 0:
        break
    union_parent(parent, p_val, p_val - 1)
    result += 1

print(result)

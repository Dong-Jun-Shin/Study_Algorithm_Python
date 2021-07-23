# 부모 노드 가져오는 연산
def find_parent(parent, e):
    if parent[e] != e:
        parent[e] = find_parent(parent, parent[e])
    return parent[e]


# 같은 팀 확인 연산 - 1
def is_equal_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return True
    else:
        return False


# 팀 합치기 연산 - 0
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 팀의 수(0~N) N, 주어진 연산 개수 M 받기
n, m = map(int, input().split())

# parent 테이블 초기화 (0 ~ N)
parent = [i for i in range(n + 1)]
operation = []

for _ in range(m):
    oper, a, b = map(int, input().split())
    operation.append((oper, a, b))

for val in operation:
    oper, a, b = val
    # 합치기 연산
    if oper == 0:
        union_parent(parent, a, b)
    # 확인 연산
    elif oper == 1:
        if is_equal_parent(parent, a, b):
            print("YES")
        else:
            print("NO")

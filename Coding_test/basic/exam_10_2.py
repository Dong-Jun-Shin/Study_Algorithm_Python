# 특정 원소가 속한 집합을 찾기
def find_parent(parent, e):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 호출
    if parent[e] != e:
        parent[e] = find_parent(parent, parent[e])
    return parent[e]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # a의 루트노드 찾기
    a = find_parent(parent, a)
    # b의 루트노드 찾기
    b = find_parent(parent, b)
    # 노드의 루트노드를 비교해서, 큰 쪽에 작은 쪽의 루트노드 삽입
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드와 간선의 개수 받기
v, e = map(int, input().split())

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(v + 1)]

# 사이클 발생 여부
cycle = False

# 간선 정보 받아서 처리
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 발생하지 않았으면, 두 원소가 속한 집합 합치기
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

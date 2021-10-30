# 길 찾기 게임
# 재귀함수의 특징을 이용한 풀이
import sys
sys.setrecursionlimit(10**6)

preorder = list()
postorder = list()
def solution(nodeinfo):
    # 유효한 레벨 y를 리스트로 루트부터 정렬(내림차순)
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    # (idx, x, y) 구성으로 이루어진 리스트를 y(내림차순), x(오름차순) 순으로 정렬
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)), key=lambda x:(-x[1][1], x[1][0]))
    order(nodes, levels, 0)
    return [preorder, postorder]

def order(nodes, levels, curlevel):
    # 현재 노드 리스트를 복사
    n = nodes[:]
    # 현재 노드를 방문
    parent = n.pop(0)
    # 전위 순회 리스트에 추가
    preorder.append(parent[0])
    # 노드 리스트에 노드가 없다면 parent가 리프 노드
    if n:
        # 현재 부모 노드를 제외한 방문 노드 리스트를 탐색
        for i in range(len(n)):
            # i번째 노드의 level(y)이 현재 순회중인 노드보다 1단계 낮으면(=자식 노드)
            if n[i][1][1] == levels[curlevel+1]:
                # i번째의 x가 부모노드의 x보다 작은 지 판단 (작으면 왼쪽 서브트리)
                if n[i][1][0] < parent[1][0]:
                    # 부모노드의 x보다 낮은 x값을 가진 노드로 리스트를 구성해서 다시 순회
                    order([x for x in n if x[1][0] < parent[1][0]], levels, curlevel + 1)
                # i번째의 x가 부모느드의 x보다 큰 지 판단 (크면 오른쪽 서브트리)
                else:
                    # 부모노드의 x보다 높은 x값을 가진 노드로 리스트를 구성해서 다시 순회
                    order([x for x in n if x[1][0] > parent[1][0]], levels, curlevel + 1)
                    # 중간에 있는 레벨에서 오른쪽 서브트리를 확인했다면, 이후는 자식 노드이므로 멈춤
                    break
    # 후위 순회 리스트에 추가
    # 모두 탐색이 되어서 가장 왼쪽 아래에 리프 노드까지 탐색이 되었을 때, 처음 실행
    # 역으로 return되면서 추가되기 떄문에 후위 순회가 구현
    postorder.append(parent[0])
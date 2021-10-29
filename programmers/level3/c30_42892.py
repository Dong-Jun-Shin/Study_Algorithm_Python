# 길 찾기 게임
# 재귀함수로 구현한 이진트리를 이용한 풀이
import sys
sys.setrecursionlimit(int(1e6))


class Node(object):
    def __init__(self, x, val):
        self.right = self.left = None
        self.x = x
        self.data = val

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x, data):
        def _insert_value(node, x, data):
            if node is None:
                node = Node(x, data)
            else:
                if x <= node.x:
                    node.left = _insert_value(node.left, x, data)
                else:
                    node.right = _insert_value(node.right, x, data)
            return node
        self.root = _insert_value(self.root, x, data)
        return self.root is not None

    # def delete(self, key):
    #     def _delete_value(node, key):
    #         if node is None:
    #             return node, False
    #         deleted = False
    #         if key == node.data:
    #             deleted = True
    #             if node.left and node.right:
    #                 # 현재 삭제할 노드, 삭제 노드의 오른쪽 서브트리
    #                 parent, child = node, node.right
    #                 while child.left is not None:
    #                     # 현재 선택된 바닥 노드의 부모, 선택된 바닥 노드
    #                     parent, child = child, child.left
    #                 # 바닥 노드의 비어있는 왼쪽 = 삭제할 노드의 왼쪽 서브트리
    #                 child.left = node.left
    #                 # 현재 선택된 바닥 노드의 부모와 삭제할 노드가 같은지 확인
    #                 if parent != node:
    #                     # 현재 선택된 바닥 노드의 부모 왼쪽 서브트리(바닥 노드) = 선택된 바닥 노드의 오른쪽 서브트리 노드
    #                     parent.left = child.right
    #                     # 바닥노드 반대편의 노드 = 삭제한 노드의 오른쪽 서브트리 노드를 이음
    #                     child.right = node.right
    #                 node = child
    #             elif node.left or node.right:
    #                 node = node.left or node.right
    #             else:
    #                 node = None
    #         elif key < node.data:
    #             node.left, deleted = _delete_value(node.left, key)
    #         else:
    #             node.right, deleted = _delete_value(node.right, key)
    #         return node, deleted
    #     self.root, deleted = _delete_value(self.root, key)
    #     return deleted
    
    def pre_order_traversal(self, pre_list):
        def _pre_order_traversal(root, pre_list):
            if root is None:
                return pre_list
            else:
                pre_list.append(root.data)
                _pre_order_traversal(root.left, pre_list)
                _pre_order_traversal(root.right, pre_list)
        _pre_order_traversal(self.root, pre_list)
    
    def post_order_traversal(self, post_list):
        def _post_order_traversal(root, post_list):
            if root is None:
                return post_list
            else:
                post_list.append(root.data)
                _post_order_traversal(root.right, post_list)
                _post_order_traversal(root.left, post_list)
        _post_order_traversal(self.root, post_list)

def solution(nodeinfo):
    nodeinfo = [(node[1], node[0], i + 1) for i, node in enumerate(nodeinfo)]
    nodeinfo.sort(reverse=True)
    bs_tree = BinarySearchTree()
    for y, x, data in nodeinfo:
        bs_tree.insert(x, data)

    pre_order_list = []
    bs_tree.pre_order_traversal(pre_order_list)
    post_order_list = []
    bs_tree.post_order_traversal(post_order_list)
    post_order_list.reverse()
    return [pre_order_list, post_order_list]


print(solution(	[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))

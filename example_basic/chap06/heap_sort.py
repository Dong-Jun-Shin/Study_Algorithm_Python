# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence


def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""


    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left]              # 루트

        parent = left
        # a[left]의 값을 자식 노드까지 계속해서 스캔하고 적정 자리에 배치
        while parent < (right + 1) // 2: # 조건에 맞지 않으면, 최하위 자식 노드
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            
            # 큰 값을 선택
            # 오른쪽 자식이 끝 노드 범위 안에 있고, 오른쪽 자식이 왼쪽보다 크면 오른쪽 자식 선택
            child = cr if cr <= right and a[cr] > a[cl] else cl
            
            if temp >= a[child]:    # 범위의 최상위 노드 값이 선택된 자식보다 작으면 멈춤
                break
            a[parent] = a[child]    # 최상위 노드 값에 자식 노드 값 삽입
            parent = child          # 자식 노드의 인덱스를 부모 노드 인덱스에 설정
        # 최상위 노드의 있던 값을 자식 노드가 있던 위치에 삽입
        a[parent] = temp            
        

    n = len(a)

    # a[i] ~ a[n - 1]을 힙으로 만들기
    # 배열의 중간부터 끝까지 힙으로 만들기
    # 배열의 중간부터 단계마다 하나씩 범위를 늘림
    for i in range((n - 1) // 2, -1, -1):       
        down_heap(a, i, n - 1)
    
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]                 # 최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a, 0, i - 1)                  # a[0] ~ a[i - 1]을 힙으로 만들기


if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                            # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)                                # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

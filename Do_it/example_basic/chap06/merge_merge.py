# 정렬을 마친 두 배열을 병합하기
# 알고리즘 구현, sorted() 함수 이용, heapq.merge() 이용

from typing import Sequence, MutableSequence


def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0                    # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)     # 각 배열의 원소 수

    while pa < na and pb < nb:              # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:                          # a에 남은 원소를 c에 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:                          # b에 남은 원소를 c에 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1


def sorted_merge(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """sorted() 함수를 이용한 병합 정렬"""
    c = list(sorted(a + b))     # a와 b를 연겨하여 오름차순으로 정렬한 것을 list로 변환하여 c에 저장


def heapq_merge(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """heapq.merge()를 이용한 병합 정렬"""
    c = list(heapq.merge(a, b))


if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    m = [None] * (len(a) + len(b))
    s = [None] * (len(a) + len(b))
    h = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, m)             # 배열 a와 b를 병합하여 m에 저장
    merge_sorted_list(a, b, s)             # 배열 a와 b를 병합하여 s에 저장
    merge_sorted_list(a, b, h)             # 배열 a와 b를 병합하여 h에 저장

    print('배열 a와 b를 병합하여 저장했습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'merge 알고리즘을 이용한 배열 m: {m}')
    print(f'sorted() 함수를 이용한 배열  s: {s}')
    print(f'heapq.merge()를 이용한 배열  h: {h}')

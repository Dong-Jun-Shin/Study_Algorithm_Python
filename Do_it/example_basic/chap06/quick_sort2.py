# 퀵 정렬 알고리즘 구현하기
# 원소 수가 9 미만이면 단순 삽입 정렬
# 시작, 중간, 끝 원소 3개의 중간값을 피벗으로 선택하는 방법

from typing import MutableSequence


def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 단순 삽입 정렬"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


def quick_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    m = select_median(a, pl, (pl +pr) // 2, pr) # 시작 원소, 중간 원소, 끝 원소
    x = a[m]

    a[m], a[pr - 1] = a[pr - 1], a[m]
    pl += 1
    pr -= 2
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: quick_sort(a, left, pr)
    if pl < right: quick_sort(a, pl, right)


def select_median(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 중앙값의 인덱스를 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2


def sort_func(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if right - left < 9:                # 원소 수가 9 미만이면 단순 삽입 정렬로 전환
        insertion_sort(a, left, right)
    else:
        quick_sort(a, left, right)


def sort(a: MutableSequence) -> None:
    """단순 삽입 정렬과 퀵 정렬을 함께 사용한 정렬"""
    sort_func(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('퀵 정렬을 합니다(원소 수가 9 미만이면 단순 삽입 정렬을 합니다).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    sort(x)                             # 배열 x를 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

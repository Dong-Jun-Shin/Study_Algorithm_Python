# 이진 삽입 정렬 알고리즘 구현하기(bisect.insort 사용)

from typing import MutableSequence
import bisect


def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)        # a.pop(i)를 빼서 이미 정렬된 상태를 유지하는 a의 0 ~ i 위치 사이에 삽입


if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)        # 배열 x를 이진 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

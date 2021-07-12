# 병합 정렬 알고리즘 구현하기

from typing import MutableSequence


def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""


    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:                            # 커서 사이에 원소가 존재
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            # (버퍼에서 사용)
            # p: 배열 앞부분 복사할 때, 복사될 버퍼 앞부분을 주목
            # j: 버퍼 앞부분과 배열 뒷부분 비교할 때 배열 뒷부분을 주목
            p = j = 0

            # (배열에서 사용)
            # i: p와 비교할 때는 배열 복사용, j와 비교할 때는 배열 뒷부분을 주목
            # k: 정렬될 배열의 앞부분부터 주목
            i = k = left

            while i <= center:
                buff[p] = a[i]:
                p += 1
                i += 1
            
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
            
    
    n = len(a)
    buff = [None] * n                   # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)            # 배열 전체를 병합 정렬
    del buff                            # 작업용 배열을 소멸


if __name__ == '__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    merge_sort(x)                       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

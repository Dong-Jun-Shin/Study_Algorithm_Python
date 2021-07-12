# 셸 정렬 알고리즘 구현하기 (묶은 그룹 중, i 인덱스를 적절한 위치에 삽입)
# 정렬 과정을 출력

from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    """셸 정렬"""
    n = len(a)
    h = n // 2
    while h > 0:
        print(f'{h}만큼 떨어진 그룹으로 묶기')
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('← ' if m == j else '← ' if m == i else '  '), end='  ')    # 원소 출력
            print(f'{a[n - 1]:2}' + ('← ' if (n - 1) == i else '  '))                            # 마지막 원소 출력

            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2


if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num        # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shell_sort(x)           # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

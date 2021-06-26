# 이진 검색 알고리즘

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0                      # left index
    pr = len(a) - 1             # right index

    while True:
        pc = (pl + pr) // 2     # center index
        if a[pc] == key:
            return pc           # 검색 성공
        elif a[pc] < key:       # 오른쪽 범위
            pl = pc + 1         # 검색 범위를 뒤쪽 절반으로 좁힘
        else:                   # 왼쪽 범위
            pr = pc - 1         # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break

    return -1                   # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:                # 이전보다 큰 값을 입력했을 때만 다음 원소 입력
                break

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

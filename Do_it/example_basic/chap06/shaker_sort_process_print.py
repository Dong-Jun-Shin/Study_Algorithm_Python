# 셰이커 정렬 알고리즘 구현하기
# 정렬 과정을 출력

from typing import MutableSequence


def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    i = 0           # 패스 횟수
    ccnt = 0        # 비교 횟수
    scnt = 0        # 교환 횟수
    n = len(a)      # 끝 인덱스
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        """← 방향"""
        print(f'패스 {i + 1}')
        for j in range(right, left, -1):
            for m in range(0, n - 1):       # 0 ~ n-1 까지 출력 (m: 현재 출력하는 원소 인덱스)
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')    # 현재 주목하고 있지 않으면 원소 사이 (공백), 주목하고 있으면 원소 사이에 교환O이면 (+), 교환X이면 (-)
            print(f'{a[n - 1]:2}')                                                                          # 마지막 원소 출력
            exchng = 0      # 패스에서 교환 횟수
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
                exchng += 1
        left = last
        i += 1
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')    # 원소 출력
        print(f'{a[n - 1]:2}')              # 마지막 원소 출력
        if exchng == 0:
            break

        """→ 방향"""
        print(f'패스 {i + 1}')
        for j in range(left, right):
            for m in range(0, n - 1):       # 0 ~ n-1 까지 출력 (m: 현재 출력하는 원소 인덱스)
                print(f'{a[m]:2}' + ('  ' if m != j else ' +' if a[j] > a[j + 1] else ' -'), end='')    # 현재 주목하고 있지 않으면 원소 사이 (공백), 주목하고 있으면 원소 사이에 교환O이면 (+), 교환X이면 (-)
            print(f'{a[n - 1]:2}')                                                                          # 마지막 원소 출력
            exchng = 0      # 패스에서 교환 횟수
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
                exchng += 1
        right = last
        i += 1
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')    # 원소 출력
        print(f'{a[n - 1]:2}')              # 마지막 원소 출력
        if exchng == 0:
            break
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shaker_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

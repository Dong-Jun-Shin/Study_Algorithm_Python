# 버블 정렬 알고리즘 구현하기(알고리즘의 개선1 - 이미 정렬이 완료된 이후의 불필요한 처리 제거)
# 정렬 과정을 출력

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    ccnt = 0        # 비교 횟수
    scnt = 0        # 교환 횟수
    n = len(a)
    for i in range(n - 1):                  # 0 ~ n-1 까지 순차적으로 정렬 (i: 패스 인덱스)
        print(f'패스 {i + 1}')
        exchng = 0      # 패스에서 교환 횟수
        for j in range(n - 1, i, -1):       # n-1 ~ i 까지 주목해서 비교 (j: 주목하는 원소 인덱스)
            for m in range(0, n - 1):       # 0 ~ n-1 까지 출력 (m: 현재 출력하는 원소 인덱스)
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')    # 현재 주목하고 있지 않으면 원소 사이 (공백), 주목하고 있으면 원소 사이에 교환O이면 (+), 교환X이면 (-)
            print(f'{a[n - 1]:2}')                                                                          # 마지막 원소 출력
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
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
    
    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

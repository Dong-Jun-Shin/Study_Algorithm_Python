# 버블 정렬 알고리즘 구현하기(알고리즘의 개선2 - 앞 부분 정렬된 원소들에 대한 불필요한 처리 제거)
# 정렬 과정을 출력

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    i = 0           # 패스 횟수
    ccnt = 0        # 비교 횟수
    scnt = 0        # 교환 횟수
    n = len(a)      # 끝 인덱스
    k = 0           # 시작 인덱스
    while k < n - 1:
        print(f'패스 {i + 1}')
        last = n - 1
        for j in range(n - 1, k, -1):
            for m in range(0, n - 1):       # 0 ~ n-1 까지 출력 (m: 현재 출력하는 원소 인덱스)
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')    # 현재 주목하고 있지 않으면 원소 사이 (공백), 주목하고 있으면 원소 사이에 교환O이면 (+), 교환X이면 (-)
            print(f'{a[n - 1]:2}')                                                                          # 마지막 원소 출력
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j                        # 마지막 교환한 위치의 오른쪽 인덱스를 last에 대입
        k = last                                # last를 시작 인덱스로 설정 (앞에 정렬된 원소들의 다음 원소로 인덱스 설정)
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')    # 원소 출력
        print(f'{a[n - 1]:2}')              # 마지막 원소 출력
        i += 1
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

# 이진 탐색으로 풀이
import sys


def binary_search(array, target, start, end):
    # 시작 인덱스가 끝 인덱스를 넘으면 None 반환
    if start > end:
        return None
    # mid 인덱스 설정
    mid = (start + end) // 2
    # array[mid]와 target이 같으면 mid 반환
    if array[mid] == target:
        return mid
    # array[mid]가 target보다 크면 왼쪽 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # array[mid]가 target보다 작은면 오른쪽 탐색
    else:
        return binary_search(array, target, mid + 1, end)


# 보유 부품 개수 n 받기
n = int(sys.stdin.readline().rstrip())
# 보유 부품 번호 받기
nList = list(map(int, sys.stdin.readline().rstrip().split()))
# 요청 부품 개수 m 받기
m = int(sys.stdin.readline().rstrip())
# 요청 부품 번호 받기
mList = list(map(int, sys.stdin.readline().rstrip().split()))


nList.sort()
for num in mList:
    if binary_search(nList, num, 0, n - 1) is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

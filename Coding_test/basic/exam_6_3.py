# 정렬할 숫자 리스트 받기
numList = list(map(int, input()))


# 퀵 정렬 구현하기
def quick_sort(numList, start, end):
    # 원소의 개수가 1개면, 정지
    if start >= end:
        return

    # 피벗 정하기
    pivot = start
    # 왼쪽 커서
    left = start + 1
    # 오른쪽 커서
    right = end

    while left <= right:
        # left <= end일 때, left가 end를 초과하면 numList[left]를 확인하기 전에 while 조건에 의해 중지됨
        # 왼쪽 커서 증가시키면서 피벗보다 큰 값을 탐색
        while left <= end and numList[pivot] >= numList[left]:
            left += 1
        # 오른쪽 커서 증가시키면서 피벗보다 작은 값을 탐색
        while right > start and numList[pivot] <= numList[right]:
            right -= 1

        # left <= end일 때, left가 end 인덱스를 넘었다는건, right보다 크다는 의미이므로, numList[left]를 확인하지 않음
        if left > right:
            # 왼쪽 커서와 오른쪽 커서가 교차하면 오른쪽 커서와 피벗을 교환
            numList[right], numList[pivot] = numList[pivot], numList[right]
        else:
            # 왼쪽 커서와 오른쪽 커서 값을 교환
            numList[left], numList[right] = numList[right], numList[left]

    # 왼쪽 그룹에 대한 퀵 정렬
    quick_sort(numList, start, right - 1)
    # 오른쪽 그룹에 대한 퀵 정렬
    quick_sort(numList, right + 1, end)


quick_sort(numList, 0, len(numList) - 1)

print(numList)

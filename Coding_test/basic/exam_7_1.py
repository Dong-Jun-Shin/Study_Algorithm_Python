# 이진 탐색 구현하기


# 재귀적인 방법으로 구현
def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search_recur(array, target, mid + 1, end)


# 반복문을 이용한 구현
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result_recur = binary_search_recur(array, target, 0, n - 1)
result_loop = binary_search_loop(array, target, 0, n - 1)

if result_recur is None:
    print("(재귀)원소가 존재하지 않습니다.")
else:
    print(f"(재귀){result_recur + 1}")

if result_loop is None:
    print("(반복)원소가 존재하지 않습니다.")
else:
    print(f"(반복){result_loop + 1}")

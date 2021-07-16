"""---------------------------------------book
# 이진 탐색으로 한 풀이
def binary_search(array, target, start, end):
    # mid(cutter 자를 길이) 설정
    mid = (start + end) // 2
    # mid(cutter)로 자를 경우, 누적 길이
    h = 0

    # start가 end를 넘으면 mid 반환
    if start > end:
        # mid = (start + end) // 2, 이전 기준점에의 누적길이에 따라 최적화
        #   (이전 binary_search에서 어떤 경우든 호출되었다면, 이전 탐색한 기준점은 target에 알맞지 않았다.)
        # 누적길이가 부족해서 시작점을 옮겼다면, start=end=mid가 되서, 이전 탐색한 기준점에서 +1한 결과
        # 누적길이가 넉넉해서 끝점을 옮겼다면, start > end가 되서, 이전 탐색한 기준점에서 -1한 결과
        return mid

    # 자를 길이에 따라 떡들을 잘라서 길이 누적
    for i in nList:
        # i > mid 는 i - mid > 0과 같다
        if i > mid:
            h += (i - mid)

    # 자른 누적 길이로 확인
    # 누적길이가 target과 같으면 mid(cutter) 반환
    if h == target:
        return mid
    # 누적길이가 target보다 많으면 mid(cutter)를 높임(오른쪽 탐색, 시작점을 옮김)
    elif h > target:
        return binary_search(array, target, mid + 1, end)
    # 누적길이가 target보다 적으면 mid(cutter)를 낮춤(왼쪽 탐색, 끝점을 옮김)
    else:
        return binary_search(array, target, start, mid - 1)


# 이진 탐색으로 한 풀이
# 떡의 개수 n, 요청 길이 m 받기
n, m = map(int, input().split())

# 떡의 개별 높이 받기
nList = list(map(int, input().split()))

start = 0
end = max(nList)

# 떡 길이 정렬
nList.sort()

# m보다 클 경우, i 반환
print(binary_search(nList, m, start, end))

"""
# ------------------------------------------me
# 순차 탐색으로 한 풀이
# 떡의 개수 n, 요청 길이 m 받기
n, m = map(int, input().split())

# 떡의 개별 높이 받기
nList = list(map(int, input().split()))

# 떡 길이 정렬
nList.sort(reverse=True)
# 가장 긴 떡의 길이(i)부터 시작해서 -1씩 감소
for cutter in range(nList[0], 0, -1):
    # 총 길이
    h = 0
    # i보다 큰 떡을 스캔하면서 차이를 누적
    for i in nList:
        gap = i - cutter
        if gap > 0:
            h += gap

    # m보다 클 경우, i 반환
    if h >= m:
        print(cutter)
        break
# --------------------------------------------

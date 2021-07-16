# 이진 탐색으로 풀이(주석 없는 버전)
def binary_search(array, target, start, end):
    mid = (start + end) // 2
    h = 0

    if start > end:
        return mid

    for i in nList:
        if i > mid:
            h += (i - mid)

    if h == target:
        return mid
    elif h > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n, m = map(int, input().split())
nList = list(map(int, input().split()))

start = 0
end = max(nList)

nList.sort()

print(binary_search(nList, m, start, end))

# 공유기 설치 (최소 gap과 최대 gap 사이에서 이진 탐색을 하는 것이 핵심)
# 1 2 3 4 5 6 7 8 9
# o o   o       o o
# i     i       i i
import bisect

n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

start = 1
end = n_list[-1] - n_list[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    val =  n_list[0]
    count = 1
    
    # 갭 차이만큼 공유기 계속 설치
    for i in range(1, n):
        if n_list[i] >= val + mid:
            val = n_list[i]
            count += 1

    if count >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

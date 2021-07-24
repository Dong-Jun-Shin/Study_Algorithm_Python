# 회의실 배정 O(NlogN) 풀이
import sys

input = sys.stdin.readline
# 회의 개수N
n = int(input().rstrip())

timeList = [0] * n
for i in range(n):
    start, end = map(int, input().rstrip().split())
    timeList[i] = (start, end)
timeList = sorted(timeList, key=lambda x: (x[1], x[0]))
# 람다를 이용한 1번째 오름차순 정렬, 2번째 오름차순 정렬 정의(내림차순은 -를 붙임)
# 똑같은 시간에 끝나는 회의가 있다면, 시작이 더 빠른 회의가 선택되도록 정렬
# 시작 시간을 정렬하지 않으면, 시작과 끝이 같은 회의가 있을 때,
# 다른 끝이 같고, 시작 시간은 다른 회의들이 선택되지 못하는 경우가 생김

# 끝 시간으로 정렬 후, 가능한 개수 체크
currentIdx = timeList[0][1]
count = 1
for i in range(1, len(timeList)):
    if currentIdx <= timeList[i][0]:
        currentIdx = timeList[i][1]
        count += 1

print(count)

# -------------------------------------------------- me
# # 회의실 배정 O(N^2) 풀이
# import sys

# input = sys.stdin.readline
# # 회의 개수N
# n = int(input().rstrip())

# timeList = [0] * n
# for i in range(n):
#     start, end = map(int, input().rstrip().split())
#     timeList[i] = (start, end)
# timeList.sort()

# # 도수그래프 이용, 0과 1로 처리
# result = 0
# startIdx = 0
# while startIdx < n:
#     currentIdx = -1
#     count = 0
#     for time in timeList[startIdx:]:
#         if currentIdx > time[0]:
#             continue
#         currentIdx = time[1]
#         count += 1
#     result = max(result, count)
#     startIdx += 1

# print(result)
# -----------------------------------------------------

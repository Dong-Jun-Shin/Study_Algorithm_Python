# 주유소
# 100점
n = int(input())
distList = list(map(int, input().split()))
feeList = list(map(int, input().split()))

preFee = feeList[0]
result = 0
# 마지막 주유소 제외: len(feeList) - 1
for i in range(len(feeList) - 1):
    # 이전 주유비보다 싼 주유비가 있으면, 주유비 갱신
    if feeList[i] < preFee:
        preFee = feeList[i]
    # 해당 주유비로 다음 주유비 갱신 전까지 거리 계산
    result += distList[i] * preFee

print(result)


# 58점
# n = int(input())
# distList = list(map(int, input().split()))
# feeList = list(map(int, input().split()))

# sortFee = sorted(feeList[:-1])

# preIdx = len(feeList) - 1
# result = 0
# for fee in sortFee:
#     idx = feeList.index(fee)
#     # 현재 최소값의 인덱스가 이전 최소값보다 큰 경우
#     # (비용 리스트에서 이미 계산한 거리에 포함된 경우)
#     if preIdx < idx:
#         continue
#     for i in range(idx, preIdx):
#         result += feeList[idx] * distList[i]
#     preIdx = idx

# print(result)

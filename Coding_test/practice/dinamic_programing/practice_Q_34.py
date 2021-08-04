# 병사 배치하기------------------------------- LIS - O(NlogN)
import bisect

n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()
dp = [soldiers[0]]

for i in range(1, n):
    if dp[-1] < soldiers[i]:
        dp.append(soldiers[i]) 
    else:
        idx = bisect.bisect_left(dp, soldiers[i])
        dp[idx] = soldiers[i]

print(n - len(dp))

# ------------------------------------------- LIS - O(N^2)
# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [1] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if soldiers[j] > soldiers[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(n - max(dp))

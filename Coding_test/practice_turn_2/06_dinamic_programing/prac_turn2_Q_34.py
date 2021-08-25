#  병사 배치하기
import bisect

n = int(input())
n_list = list(map(int, input().split()))
n_list.reverse()
dp = [n_list[0]]

for i in range(1, n):
    if dp[-1] < n_list[i]:
        dp.append(n_list[i])
    else:
        idx = bisect.bisect_left(dp, n_list[i])
        dp[idx] = n_list[i]

print(n - len(dp))

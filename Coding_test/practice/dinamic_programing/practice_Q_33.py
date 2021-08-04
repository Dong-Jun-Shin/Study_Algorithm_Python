# 퇴사
n = int(input())
t_list = []
p_list = []
dp = [0] * (n + 1)
max_value = 0
for _ in range(n):
    data = list(map(int, input().split()))
    t_list.append(data[0])
    p_list.append(data[1])

for i in range(n - 1, -1, -1):
    time = t_list[i] + i
    if time <= n:
        dp[i] = max(p_list[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    

print(max_value)

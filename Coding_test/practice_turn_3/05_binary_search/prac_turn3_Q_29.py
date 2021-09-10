# 공유기 설치
n, c = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
n_list.sort()

l_idx = 1
r_idx = n_list[-1] - n_list[0]
max_dist = 0
while r_idx >= l_idx:
    seper_dist = (l_idx + r_idx) // 2
    now = n_list[0] + seper_dist
    count = 1
    for n_val in n_list[1:]:
        if now <= n_val:
            now = n_val + seper_dist
            count += 1
    if count >= c:
        max_dist = seper_dist
        l_idx = seper_dist + 1
    else:
        r_idx = seper_dist - 1

print(max_dist)

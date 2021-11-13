start = 1
end = len(n_list)
max_dist = 0
while start <= end:
    mid = (start + end) // 2
    for n_val in n_list:
        if now <= n_val:
            now = n_val + mid
            count += 1

    if count >= c:
        max_dist = mid
        start = mid + 1
    else:
        end = mid - 1
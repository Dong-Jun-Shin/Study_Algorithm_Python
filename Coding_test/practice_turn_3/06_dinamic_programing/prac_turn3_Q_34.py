# 병사 배치하기
import bisect

n = int(input())
n_list = list(map(int, input().split()))
lis = [n_list[-1]]

for n_val in n_list[::-1]:
    if lis[-1] >= n_val:
        idx = bisect.bisect_left(lis, n_val)
        lis[idx] = n_val
    else:
        lis.append(n_val)    

print(n - len(lis))

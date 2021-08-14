# 카드 정렬하기
import heapq

n = int(input())
n_list = []
for _ in range(n):
    heapq.heappush(n_list, int(input()))

sum_val = 0
while len(n_list) > 1:
    n_val_1 = heapq.heappop(n_list)
    n_val_2 = heapq.heappop(n_list)
    sum_val += n_val_1 + n_val_2
    heapq.heappush(n_list, n_val_1 + n_val_2)

print(sum_val)

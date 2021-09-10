#  카드 정렬하기
import heapq

n = int(input())
n_list = []
for _ in range(n):
    heapq.heappush(n_list, int(input()))

tot_cmp = 0
while len(n_list) > 1:
    cost_a = heapq.heappop(n_list)
    cost_b = heapq.heappop(n_list)
    tot_cmp += cost_a + cost_b
    heapq.heappush(n_list, cost_a + cost_b)

print(tot_cmp)

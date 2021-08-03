# 카드 정렬하기(카드를 합치면, 그 값을 포함하는 새로운 리스트로 보고 최소수를 합치는게 핵심)
import heapq

n = int(input())
num_list = []
for _ in range(n):
    heapq.heappush(num_list, int(input()))

if n == 1:
    print(0)
else:
    result = 0
    while len(num_list) > 1:
        num1 = heapq.heappop(num_list)
        num2 = heapq.heappop(num_list)
        
        sum_num = num1 + num2

        result += sum_num
        heapq.heappush(num_list, sum_num)

    print(result)

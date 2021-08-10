# 볼링공 고르기
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
array = [0] * (n + 1)

for n_val in n_list:
    array[n_val] += 1

result = 0
for i in range(1, n + 1):
    n -= array[i]
    result += array[i] * n

print(result)

# -------------------------------------- me
# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))

# result = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if n_list[i] == n_list[j]:
#             continue
#         result += 1

# print(result)
# -----------------------------------------

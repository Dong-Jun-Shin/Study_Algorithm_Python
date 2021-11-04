# 벌집
n = int(input())
answer = 1
cnt = 1
while n > answer:
    answer += 6 * cnt
    cnt += 1
print(cnt)

# n = int(input())
# answer = 1
# intervals = [(2, 7)]
# i = 7
# multiple_idx = 12

# while n > intervals[-1][1]:
#     intervals.append((i + 1, i + multiple_idx))
#     i += multiple_idx
#     multiple_idx += 6

# for i in range(len(intervals)):
#     if intervals[i][0] <= n <= intervals[i][1]:
#         answer += i + 1
#         break

# print(answer)

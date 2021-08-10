# 모험가 길드
n = int(input())
n_list = list(map(int, input().split()))

n_list.sort(reverse=True)

result = 0
i = 0
while i < n:
    i += n_list[i]
    result += 1

print(result)

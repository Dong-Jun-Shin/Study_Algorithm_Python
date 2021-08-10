# 만들 수 없는 금액
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

result = n_list[0]
for n_val in n_list[1:]:
    if result < n_val:
        break
    result += n_val
    
print(result + 1)

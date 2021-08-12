# 연산자 끼워넣기
def dfs(num, idx):
    global max_val, min_val, add, sub, mul, div
    if add != 0:
        add -= 1
        dfs(num + n_list[idx], idx + 1)
        add += 1
    if sub != 0:
        sub -= 1
        dfs(num - n_list[idx], idx + 1)
        sub += 1
    if mul != 0:
        mul -= 1
        dfs(num * n_list[idx], idx + 1)
        mul += 1
    if div != 0:
        div -= 1
        dfs(int(num / n_list[idx]), idx + 1)
        div += 1

    if idx == len(n_list):
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    


n = int(input())
n_list = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

max_val = int(-1e9)
min_val = int(1e9)
dfs(n_list[0], 1)

print(max_val)
print(min_val)

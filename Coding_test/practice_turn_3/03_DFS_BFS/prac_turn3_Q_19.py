# 연산자 끼워넣기
from itertools import permutations

n = int(input())
n_list = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))
oper = ['+', '-', '*', '/']
oper_list = []
for i in range(4):
    for _ in range(oper_cnt[i]):
        oper_list.append(oper[i])

cases = list(permutations(oper_list, len(oper_list)))
cases = list(set(cases))

max_value = int(-1e9)
min_value = int(1e9)
for case in cases:
    total = n_list[0]
    for i in range(1, n):
        if case[i - 1] == '+':
            total += n_list[i]
        elif case[i - 1] == '-':
            total -= n_list[i]
        elif case[i - 1] == '*':
            total *= n_list[i]
        elif case[i - 1] == '/':
            total = int(total / n_list[i])
    max_value = max(max_value, total)
    min_value = min(min_value, total)

print(max_value)
print(min_value)

# 연산자 끼워 넣기 (DFS 방식이 순열 + 브루트포스 방식보다 10배정도 빠르고, 메모리도 6배 정도 적게 사용)
# (DFS, BFS, 중복순열 + 브루트포스로 풀이 가능)
import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = int(-1e9)
min_value = int(1e9)
def dfs(i, now):
    global max_value, min_value, add, sub, mul, div
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / num_list[i]))
            div += 1
            
dfs(1, num_list[0])

print(max_value)
print(min_value)

# -------------------------------------------------------------------------------------- me
# from itertools import permutations
# import sys

# input = sys.stdin.readline
# n = int(input())
# num_list = list(map(int, input().split()))
# oper_len = list(map(int, input().split()))
# oper_list = list("+" * oper_len[0] + "-" * oper_len[1] + "*" * oper_len[2] + "/" * oper_len[3])

# max_value = int(-1e9)
# min_value = int(1e9)
# for cases in list(permutations(oper_list, len(oper_list))):
#     result = num_list[0]
#     for i in range(len(cases)):
#         if cases[i] == "+":
#             result += num_list[i + 1]
#         elif cases[i] == "-":
#             result -= num_list[i + 1]
#         elif cases[i] == "*":
#             result *= num_list[i + 1]
#         elif cases[i] == "/":
#             if result < 0:
#                 result *= -1
#                 result //= num_list[i + 1]
#                 result *= -1
#             else:
#                 result //= num_list[i + 1]
    
#     max_value = max(max_value, result)
#     min_value = min(min_value, result)
            
# print(max_value)
# print(min_value)
# -----------------------------------------------------------------------------------------

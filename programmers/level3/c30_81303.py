# 표 편집
# 딕셔너리를 이용해서 구현한 더블 링크드리스트 풀이
def solution(n, k, cmds):
    d_link = {i: [i - 1, i + 1] for i in range(n)}
    table = ['O' for _ in range(n)]
    recovery = []
    for cmd in cmds:
        cmd = cmd.split()
        if cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                k = d_link[k][0]
        elif cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                k = d_link[k][1]
        elif cmd[0] == 'C':
            prev, next = d_link[k]
            recovery.append([prev, next, k])
            table[k] = 'X'
            if prev == -1:
                d_link[next][0] = prev
            elif next == n:
                d_link[prev][1] = next
            else:
                d_link[next][0] = prev
                d_link[prev][1] = next
            
            # 삭제 후, 인덱스 조정
            if d_link[k][1] == n:
                k = d_link[k][0]
            else:
                k = d_link[k][1]
        elif cmd[0] == 'Z':
            prev, next, val = recovery.pop()
            table[val] = 'O'
            if prev == -1:
                d_link[next][0] = val
            elif next == n:
                d_link[prev][1] = val
            else:
                d_link[next][0] = val
                d_link[prev][1] = val
    return ''.join(table)

# 리스트를 사용(시간 초과)
# def solution(n, k, cmds):
#     table = ['O' for _ in range(n)]
#     length = n - 1
#     recovery = []
#     for cmd in cmds:
#         cmd = cmd.split()
#         if cmd[0] == 'U':
#             # 커서 위 이동
#             o_cnt = int(cmd[1])
#             for i in range(k - 1, -1, -1):
#                 if table[i] == 'X':
#                     k -= 1
#                 else:
#                     o_cnt -= 1
#                 if o_cnt == 0:
#                     break
#             k -= int(cmd[1])
#         elif cmd[0] == 'D':
#             # 커서 아래 이동
#             o_cnt = int(cmd[1])
#             for i in range(k + 1, len(table)):
#                 if table[i] == 'X':
#                     k += 1
#                 else:
#                     o_cnt -= 1
#                 if o_cnt == 0:
#                     break
#             k += int(cmd[1])
#         elif cmd[0] == 'C':
#             # 삭제 기능
#             recovery.append(k)
#             table[k] = 'X'
#             if k == length:
#                 idx = ''.join(table).rfind('O')
#                 k = idx
#                 length = idx
#             else:
#                 k += 1
#         elif cmd[0] == 'Z':
#             # 복구 기능
#             re_idx = recovery.pop()
#             table[re_idx] = 'O'
#             if re_idx > length:
#                 length = ''.join(table).rfind('O')
#     return ''.join(table)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(8, 6, ["C", "C", "C", "U 4", "C", "Z", "Z", "U 1", "C"]))

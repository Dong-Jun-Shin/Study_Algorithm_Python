# 여행경로
# DFS - 순서를 탐색
from collections import defaultdict


def solution(tickets):
    ticket_dict = defaultdict(list)
    for start, end in tickets:
        ticket_dict[start].append(end)
    for start in ticket_dict:
        ticket_dict[start].sort()
    stack = ["ICN"]
    answer = []
    while stack:
        start = stack[-1]
        if ticket_dict[start]:
            stack.append(ticket_dict[start].pop(0))
        else:
            answer.append(stack.pop())
    return answer[::-1]


# DFS - 순서를 탐색
# from collections import defaultdict

# def dfs(n, ticket_dict, start, now_path):
#     if len(now_path) == n + 1:
#         return now_path

#     end_path = ticket_dict[start][:]
#     for end in end_path:
#         now_path.append(end)
#         ticket_dict[start].remove(end)
#         result = dfs(n, ticket_dict, end, now_path)
#         if result:
#             return result
#         ticket_dict[start].append(end)
#         now_path.pop()

# def solution(tickets):
#     ticket_dict = defaultdict(list)
#     for start, end in tickets:
#         ticket_dict[start].append(end)
#     for start in ticket_dict:
#         ticket_dict[start].sort()
#     n = len(tickets)
#     return dfs(n, ticket_dict, "ICN", ["ICN"])


# BFS (테스트 케이스 1 실패)
# from collections import defaultdict, deque

# def solution(tickets):
#     answer = ["ICN"]
#     ticket_dict = defaultdict(list)
#     indegree = defaultdict(int)
#     for start, end in tickets:
#         ticket_dict[start].append(end)
#         indegree[start] += 1

#     q = deque()
#     q.append("ICN")
#     while q:
#         start = q.popleft()
#         indegree[start] -= 1
#         end_list = ticket_dict[start]    
#         available = []
#         for end in end_list:
#             if indegree[end] >= 1:
#                 available.append((indegree[end], end))
#         available.sort(key=lambda x:(-x[0], x[1]))
#         if available:
#             end_list.remove(available[0][1])
#             answer.append(available[0][1])
#             q.append(available[0][1])
#         else:
#             answer.append(end)
#     return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))
print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))

# 실패율
# (스테이지에 도달한 사람이 0일 때, 남은 사람이 0일 때, 완료한 사람은 N + 1의 값을 갖는 점에 주의)
def solution(N, stages):
    answer = []
    people = len(stages)
    graph = [0] * (N + 2)
    for stage in stages:
        graph[stage] += 1

    failure_list = []
    for i in range(1, N + 1):
        if people > 0:
            failure_late = graph[i] / people
        elif graph[i] <= 0:
            failure_late = 0
        
        people -= graph[i]

        if i <= N:
            failure_list.append((failure_late, i))

    failure_list.sort(key=lambda x: (-x[0], x[1]))
    for failure in failure_list:
        answer.append(failure[1])
    return answer

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))

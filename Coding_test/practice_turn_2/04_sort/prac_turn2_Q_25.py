# 실패율
def solution(N, stages):
    answer = []
    temp = []
    length = len(stages)
    graph = [0] * (N + 2)
    for stage in stages:
        graph[stage] += 1

    for i in range(1, N + 1):
        if length < 1:
            failure = 0
        else:
            failure = graph[i] / length
        if graph[i] == 0:
            temp.append((0, i))
        else: 
            temp.append((failure, i))
        length -= graph[i]
    
    temp.sort(key=lambda x:(-x[0], x[1]))
    for val in temp:
        answer.append(val[1])

    return answer


N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))

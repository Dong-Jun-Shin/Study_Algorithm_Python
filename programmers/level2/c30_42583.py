# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    going_time = []
    going_sum = []
    while truck_weights:
        answer += 1
        if going_time and answer >= going_time[0]:
            going_time.pop(0)
            going_sum.pop(0)

        if truck_weights:
            next_val = truck_weights.pop()
            if sum(going_sum) + next_val <= weight and len(going_time) + 1 <= bridge_length:
                going_sum.append(next_val)
                going_time.append(bridge_length + answer)
            else:
                truck_weights.append(next_val)

    answer += bridge_length
    return answer


print(solution(2, 10, [7, 4, 5, 6]))

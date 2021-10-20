# 오픈채팅방
def solution(record):
    answer = []
    orders = []
    user = {}
    for string in record:
        datas = list(string.split())
        if datas[0] != 'Change':
            orders.append([datas[0], datas[1]])
        if datas[0] != 'Leave':
            user[datas[1]] = datas[2]
    for order, id in orders:
        string = f'{user[id]}님이 '
        if order == 'Enter':
            string += '들어왔습니다.'
        else:
            string += '나갔습니다.'
        answer.append(string)
    return answer

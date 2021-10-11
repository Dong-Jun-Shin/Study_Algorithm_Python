# 뉴스 클러스터링
# 다중중복 처리때문에 set을 사용할 수 없음
# 문제 요구사항에 맞게, list로 합집합과 교집합을 구현
# list로 집합연산을 할 때, for문에 사용중인 리스트 원소를 
#     제거하거나 늘리면 원소의 인덱스들이 달라져서 결과가 달라짐
import copy


def get_list(string):
    x_list = []
    for i in range(len(string)):
        e = string[i:i + 2]
        if len(e) == 2:
            if ord('a') <= ord(e[0]) <= ord('z'):
                if ord('a') <= ord(e[1]) <= ord('z'):
                    x_list.append(e)
    return x_list


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    a_list = get_list(str1)
    b_list = get_list(str2)
    inter_list = []
    union_list = []
    copy_a_list = copy.deepcopy(a_list)
    copy_b_list = copy.deepcopy(b_list)
    for e in a_list:
        if e in copy_b_list:
            inter_list.append(e)
            copy_a_list.remove(e)
            copy_b_list.remove(e)
    union_list = inter_list + copy_a_list + copy_b_list
    inter_leng = len(inter_list)
    union_leng = len(union_list)
    if union_leng == 0:
        answer = 1
    else:
        answer = inter_leng / union_leng
    return int(answer * 65536)

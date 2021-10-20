# 후보키
# set과 len을 이용한 중복 체크
# any, all을 이용한 튜플끼리의 부분집합 여부 체크
from itertools import combinations, chain


def is_case(except_cases, case):
    answer = []
    for except_case in except_cases:
        # except_case가 그대로 포함된 경우를 찾기
        answer.append(all(exc_idx in list(case) for exc_idx in except_case))
    # except_cases에서 포함된 경우가 한번이라도 있으면 해당 case는 제외
    return any(answer)


def is_p_key(col):
    return len(col) == len(set(col))


def solution(relation):
    col_leng = len(relation[0])

    # col으로 분리
    col_list = [[] for _ in range(col_leng)]
    for row in relation:
        for i in range(col_leng):
            col_list[i].append(row[i])

    # col의 조합
    cases = []
    for i in range(1, col_leng + 1):
        cases.append(combinations(range(col_leng), i))
    cases = list(chain(*cases))

    # 후보키 찾기
    except_cases = []
    for case in cases:
        # 확인된 후보키를 사용하는지, 최소성 확인
        if is_case(except_cases, case):
            continue
        # 현재 case에 해당하는 컬럼 조합 생성
        case_col = []
        for idx in case:
            case_col.append(col_list[idx])
        case_col = list(zip(*case_col))
        # 현재 컬럼 조합의 유일성 확인
        if is_p_key(case_col):
            except_cases.append(case)
    return len(except_cases)


relation = [['a', 'aa'], ['aa', 'a'], ['a', 'a']]
print(solution(relation))

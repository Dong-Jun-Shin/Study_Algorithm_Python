# 입력
n = input()     # return (String)

# 자료형 변환
list(), set(), str(), int(), float(), dict()

# 큐
# 우선순위큐
import heapq
heapq.heapify(q_list)
heapq.heappush(q_list, val)
heapq.heappop(q_list)
# 덱
from collections import deque
q_list = deque()
q_list.append(val)
q_list.popleft()
q_list.pop()

# 정렬
# (정렬기준, 역정렬)
n_list.sort(key=lambda x: (x[0], -x[1]), reverse=True)
sorted(n_list, key=lambda x: (x[0], -x[1]), reverse=True)

# 범위
# (시작, 끝, 증가값)
n = range(0, len(n), 1)     # return (list)

# 포함여부 확인
n_bool = n in n_list

# 전체 적용
# (함수, 리스트)
n = list(map(max, list))     # return ([max(list[i])])

# 제네레이터
# [원소 for문 if문]
n = [i for i in range(n) if i < 5]  # True인 원소만으로 구성된 리스트를 반환(yield를 활용)

# for문 이터레이터
range(0, len(n))    # 0부터 n - 1까지 하나씩 반환
n_list              # 원소를 하나씩 반환
[-1, 1]             # 원소를 하나씩 반환

# 람다
# lambda 인자: (함수 내용)(전달 인자)
lambda s, e: (i for i in range(s, e))(1, 5)     # return [1, 2, 3, 4]

# 여러개 리스트를 하나로 이어 붙이기
# 리스트 연산 이용
n_list = a_list + b_list                # return [(a_list)(b_list)]
# 리스트 함수 이용
n_list = a_list.extend(b_list)          # return ([(a_list)(b_list)]
# chain 이용
from itertools import chain
n_list = chain(a_list, b_list, c_list)  # return ([(a_list)(b_list)(c_list)]

# 여러개 리스트를 원소끼리 합치기
n_list = zip(a_list, b_lsit, c_list)    # return ([(a_list[0], b_list[1], c_list[0]), (), ()...])

# 리스트 복사
import copy
deepcopy_list = n_list[:]               # 리스트 슬라이싱을 이용한 카피
deepcopy_list = copy.deepcopy(n_list)

# 기본 사전형
# (자료형)
from collections import defaultdict
n = defaultdict(list)

# 개수 세기
# 리스트 함수를 이용
n_list.count(val)                               # val의 개수를 반환
# 이진탐색을 이용
import bisect
right_idx = bisect.bisect_right(n_list, end)
left_idx = bisect.bisect_left(n_list, start)
cnt = right_idx - left_idx

# 순열과 조합
from itertools import permutations, combinations
p_case = permutations(n_list)   # 순서 바꾼 값을 동일하게 보지 않은 모든 경우의 수
c_case = combinations(n_list)   # 순서 바꾼 값을 동일하게 보고 제외하는 경우의 수

# 카테시안 곱(데카르트 곱, 곱집합)
from itertools import product
n_case = product(a_list, b_list, c_list)    # return ([(a_list[0], b_list[0], c_list[0]), (a_list[0], b_list[0], c_list[1]), ()...])

# list 연산
n_list = a_list + b_list    # [(a_list)(b_list)]
n_list = n_list * 3         # [(n_list)(n_list)...]

n_list.append(val)          # val을 리스트 끝에 추가
n_list.insert(idx, val)     # idx번째 위치에 val를 추가
n_list.remove(val)          # 리스트에서 처음 발견한 val과 동일한 원소를 제거
n_list.pop()                # 리스트 끝의 값을 삭제하고 반환
n_list.pop(i)               # 리스트 i번째 값을 삭제하고 반환
del n_list[i]               # 리스트 i번째 값을 삭제
n_list.reverse()            # 리스트 뒤집기
n_list.index(val)           # val이 위치한 첫번째 인덱스 반환 (없을 시, ValueError)
n_list.find(val)            # val이 위치한 첫번째 인덱스 반환 (없을 시, -1)
n_list.count(val)           # val의 개수를 반환

# set 연산
# 합집합 - a_set과 b_set의 모든 원소 반환
n_set = a_set | b_set
n_set = set.union(a_set, b_set)
n_set = a_set.union(b_set)
# 교집합 - a_set과 b_set의 공통 원소 반환
n_set = a_set & b_set
n_set = set.intersection(a_set, b_set)
n_set = a_set.intersection(b_set)
# 차집합(왼쪽만, 오른쪽만) - a_set의 남는 원소 반환
n_set = a_set - b_set
n_set = set.difference(a_set, b_set)
n_set = a_set.difference(b_set)
# 대칭차집합 - 교집합을 제외한 원소를 반환
n_set = a_set ^ b_set                   # XOR 연산
n_set = set.symmetric_difference(a_set, b_set)
n_set = a_set.symmetric_difference(b_set)

n_set.add(val)          # 단일값 추가
n_set.update(n_list)    # 리스트 추가
n_set.remove(val)       # 단일값 삭제

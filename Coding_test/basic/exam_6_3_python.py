# 정렬할 숫자 리스트 받기
numList = list(map(int, input()))


def quick_sort_py(numList):
    # 전달받은 리스트의 원소가 1개만 남으면 반환
    if len(numList) <= 1:
        return numList

    # 피벗 선택
    pivot = numList[0]
    # 피벗을 제외한 전체 리스트
    tail = numList[1:]

    # 리스트 컴프리헨션을 통한 좌우 그룹 초기화
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 반환된 리스트들과 피벗 리스트를 결합해서 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


# 반환된 리스트를 numList에 삽입
numList = quick_sort_py(numList)
print(numList)

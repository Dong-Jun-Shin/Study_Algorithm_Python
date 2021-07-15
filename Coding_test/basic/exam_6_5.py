# 정렬할 숫자 리스트 받기
arr = [('바나나', 2), ('사과', 5), ('당근', 3)]


# sorted 함수 사용 시, 여러개의 데이터로 구성된 리스트에
# 기준이 될 데이터를 함수 형태를 이용해서 선택해줄 수 있다.
def setting(data):
    return data[1]


result = sorted(arr, key=setting)

print(result)

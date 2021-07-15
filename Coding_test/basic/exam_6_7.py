"""---------------------------------------book
# 학생 수 받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')

"""
# ------------------------------------------me


# 정렬 시, 기준으로 사용할 키 설정
def setting(data):
    return data[1]


# 학생 수 받기
studentCount = int(input())

# 이름과 성적 받기
gradeList = []
for i in range(studentCount):
    gradeList.append(list(input().split()))


gradeList = sorted(gradeList, key=setting)

for i in gradeList:
    print(i[0], end=' ')
# --------------------------------------------

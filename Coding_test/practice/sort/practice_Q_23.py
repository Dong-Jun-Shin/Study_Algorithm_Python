# 국영수
n = int(input())
student_info_list = []
for i in range(n):
    data = list(input().split())
    for j in range(1, len(data)):
        data[j] = int(data[j])
    student_info_list.append(data)

student_info_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(len(student_info_list)):
    print(student_info_list[i][0])

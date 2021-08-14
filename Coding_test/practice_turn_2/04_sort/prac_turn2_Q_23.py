# 국영수
import sys
input = sys.stdin.readline

n = int(input())
grade_list = []
for _ in range(n):
    datas = list(input().split())
    grade_list.append((datas[0], int(datas[1]), int(datas[2]), int(datas[3])))

grade_list.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for grade in grade_list:
    print(grade[0])

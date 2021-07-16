# 집합을 이용한 풀이
import sys

# 보유 부품 개수 n 받기
n = int(input())

# 보유 부품 번호를 받아서 리스트에 삽입
nList = set(map(int, input().split()))

# 요청 부품 개수 m 받기
m = int(sys.stdin.readline().rstrip())
# 요청 부품 번호 받기
mList = list(map(int, sys.stdin.readline().rstrip().split()))

for num in mList:
    if num in nList:
        print("yes", end=' ')
    else:
        print("no", end=' ')

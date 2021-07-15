# 배열 원소 개수 n, 교환 가능 횟수 k 받기
n, k = map(int, input().split())

# 배열 A와 B를 입력받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# 전체 원소 개수를 정렬했을 때, 교환할 가장 큰 값 k개가 시작되는 인덱스
# enumerate() : 배열을 받아서, (index, value) 형태로 순차 반환
for idx, val in enumerate(B[n - k:]):
    # 교환이 시작될 인덱스를 빼서, A는 0부터 시작, B는 교환 인덱스에서 시작
    A[idx] = val

# result = 0
# for i in A:
#     result += i
# print(result)
print(sum(A))

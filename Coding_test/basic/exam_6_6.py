# 수열 사이즈 입력받기
seqSize = int(input())

# 수열 입력받기
sequence = []
for i in range(seqSize):
    sequence.append(int(input()))

# 오름차순 정렬 및 역순
sequence = sorted(sequence, reverse=True)

# 오름차순 정렬 및 역순으로 정렬(내림차순)
# sequence.sort()
# sequence.reverse()


# 수열 출력
for i in sequence:
    print(i, end=' ')

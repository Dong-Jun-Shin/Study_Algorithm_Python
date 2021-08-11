# 럭키 스트레이트
score = list(map(int, input()))
n = len(score) // 2

if sum(score[:n]) == sum(score[n:]):
    print("LUCKY")
else:
    print("READY")

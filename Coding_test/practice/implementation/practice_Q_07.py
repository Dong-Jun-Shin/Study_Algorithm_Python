# 럭키 스트레이트
n = input()

leftNum = list(map(int, n[:len(n)//2]))
rightNum = list(map(int, n[len(n)//2:]))

if sum(leftNum) == sum(rightNum): 
    print("LUCKY")
else:
    print("READY")

# 멀쩡한 사각형
# 가로, 세로를 GCD번 나눈 가로', 세로'의 패턴이 반복된다.
# 가로', 세로'의 대각선이 가로지르는 사각형 개수는 최단거리이다.
# 대각선 최단거리는 시작하는 사각형 1개, 아래 이동 횟수, 오른쪽 이동 횟수이다.
# 1 + (가로 - 1) + (세로 - 1) = 가로 + 세로 - 1
import math


def solution(w,h):
    answer = 0
    if w == 0 or h == 0 or w == 1 or h == 1:
        return 0
    gcd_val = math.gcd(w, h)
    # w * h - (w//gcd_val + h//gcd_val - 1)
    answer = w * h - (w + h - gcd_val)
    return answer

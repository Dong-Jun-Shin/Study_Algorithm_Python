# 스택으로 재귀 함수 구현하기(재귀를 제거)

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#print(__file__)                                                         # 현재 파일의 위치 반환
#print(os.path.dirname(__file__))                                        # 파일이 위치한 경로명 반환
#print(os.path.abspath(os.path.dirname(__file__)))                       # 특정 경로에 대한 절대 경로 반환
#print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))      # 해당 절대 경로가 위치한 경로 반환

from chap04.stack import Stack


def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break


x = int(input('정숫값을 입력하세요.: '))

recur(x)

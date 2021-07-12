# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recursion의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


def recur_reverse(n: int) -> int:
    """재귀 함수 결과를 역순으로 출력하기"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)


x = int(input('정숫값을 입력하세요.: '))

recur(x)

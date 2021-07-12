# 양의 정수 n의 팩토리얼 구하기

def factorial(n: int) -> int:
    """양의 정수n의 팩토리얼값을 재귀적으로 구현"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 1:
        return 1
    else:
        raise ValueError


if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.: '))
    try:
        print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
    except ValueError:
        print(f'입력한 수는 정수가 아닙니다.')

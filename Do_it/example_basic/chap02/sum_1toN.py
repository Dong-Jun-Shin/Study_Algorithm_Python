# 1부터 n까지 정수의 합 구하기
# 매개변수 전달 시, immutable 객체를 참조하는 변수의 경우, 다른 객체를 생성해서 참조값을 변환 (int, float 등등)

def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0:
        s += n
        n -= 1
        return s


x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')

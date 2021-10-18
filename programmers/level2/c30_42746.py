# 가장 큰 수
# 숫자를 비교할 때, 999 99 9 998 997 996...으로 진행
# 9 998 997 > *3 > 999 998998998 997997997
# ASCII에 의해 999 998 997로 비교되서 정렬
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x:x*3, reverse=True)
#     return str(eval(''.join(numbers)))


# functools.cmp_to_key를 이용해서 크면 1, 같으면 0, 작으면 -1 나오는 
#     함수를 정의해서 sorted의 key로 사용 가능
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    print(t1, t2, (int(t1) > int(t2)) - (int(t1) < int(t2)))
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

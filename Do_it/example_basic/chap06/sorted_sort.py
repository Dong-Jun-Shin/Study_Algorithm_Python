# sorted() 함수를 사용하여 정렬하기

print('sorted() 함수를 사용하여 정렬합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num        # 원소 수가 num인 배열을 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
y = tuple(x)

"""배열 x를 오름차순으로 정렬"""
x = sorted(x)
print('오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')


"""배열 x를 내림차순으로 정렬"""
x = sorted(x, reverse = True)
print('내림차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')


"""튜플 y를 정렬"""
y = tuple(sorted(y))
print('튜플을 오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'y[{i}] = {y[i]}')
x = ['John', 'George', 'Paul', 'Ringo']

# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
print('-' * 20)

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
print('-' * 20)

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)
for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
print('-' * 20)

# 리스트의 모든 원소를 스캔하기(인덱스값을 사용하지 않음)
for i in x:
    print(i)
print('-' * 20)


# 역순 스캔 reversed(x), x[::-1]
# 시간 성능 측정
import time

start_time = time.time()

for _ in range(1, 10000000):
    a = 1

end_time = time.time()

print(f'실행에 소요된 시간은 {end_time - start_time} 입니다.')

import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()

# H 입력 받기
h = int(input('1시~23시 사이 시간 입력 : '))
count = 0
for i in range(h + 1): # 시간 
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3'이 하나라도 포함되어 있다면 참
                count += 1 # 카운트 증가
        print(count)
print('최종 3이 카운트 된 결과는 :', count)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력




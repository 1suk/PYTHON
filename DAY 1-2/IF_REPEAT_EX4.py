a = int(input("정수 1개를 입력 받아 1부터 그 수까지 쩍수의 합을 출력하시오:"))
for i in range(1,a):
    if i % 2 == 0:
        continue
        
print(i)

n = int(input('1~100'))
sum = 0
for i in range(n+1):
    if(i%2)
a = int(input("1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오:"))
total = 0

for i in range(1, a):
	if i % 2 ==0:
	    total += i

print(total)

while True:
    a = input("영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오:")
    a = str(a)
    if(a == 'q'):
        break
    else:
	    print(a)
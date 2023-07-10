a, b, c = map(int, input('3개 정수 입력 : ').split()) # 실수 2개 입력 받음
a=int(a)
b=int(b)
c=int(c)
total=a+b+c # 변수에 합 저장
avg=total/3 # 변수에 평균 저장
print(total, format(avg, ".2f")) # 합산 결과와 평균(소수점 2자리) 출력

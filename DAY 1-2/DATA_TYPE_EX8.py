lst = []
tuple_a = ()

while True:
    name = input("저장할 이름을 입력 : ")
    if name == '':
        break
    lst.append(name)

print("입력한 이름의 전체 목록 :")
for name in lst:
	print(name, ',')


print("튜플로 캐스팅 후 출력 :")
tuple_a = tuple(lst)
for i in tuple_a:
	print(i, end=',')
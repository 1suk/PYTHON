list = [ ]

while True:
	name = input("저장할 이름을 입력 : ")
	if name == '':
	    break
	list.append(name)

print("입력한 이름의 전체 목록 :")
for name in list:
	print(name, end=',')
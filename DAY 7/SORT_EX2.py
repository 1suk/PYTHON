n = int(input("입력할 정수의 개수를 입력하시오:"))
array = []

for _ in range(n):
    array.append(int(input()))
        
sorted_array = sorted(array, reverse = True)
        
for i in sorted_array:
        print(i, end = ',')

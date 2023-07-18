from bisect import bisect_left, bisect_right
n = int(input("입력할 원수의 개수:"))
value = int(input("어떤 원수 개수:"))
array = []

for i in range(n):
    array.append(int(input("값을 입력하기")))

def count_by_value(array, value):
    left_index = bisect_left(array, value)
    right_index = bisect_right(array, value)
    return right_index - left_index  # 특정 값의 개수 반환

count = count_by_value(array, value)
print("특정 값의 개수는 {}입니다.".format(count))

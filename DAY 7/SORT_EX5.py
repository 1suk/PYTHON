'''n = int(input("부품의 개수를 입력하시오:"))
n_list = []
for _ in range(n):
    x = int(input())
    n_list.append(x)

m= int(input("손님이 찾는 제품의 개수를 입력하시오:"))
m_list = []
for _ in range(m):
    y = int(input())
    m_list.append(y)
    

print("부품 유무:")
for y in m_list:    
    if y in n_list:
        print("yes")
    else:
        print("no")

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

print("부품 유무:")
n_list.sort()  # 이진 탐색을 위해 리스트를 정렬합니다.

for y in m_list:
    if binary_search(n_list, y):
        print("yes")
    else:
        print("no")'''

import sys
import bisect

si = sys.stdin.readline
n = int((si())
store = sorted(map(int, si().split()))
m = int(si())
wish = list(map(int, si().split()))

for x in wish:
    idx = bisect.bisect_left(store,x)
    
    if store[idx] == x:
        print('yes', end = '')
    else:
        print('no', end = '')


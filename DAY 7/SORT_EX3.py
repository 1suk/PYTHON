n = int(input("회원의 수를 작성하시오:"))
member_list = []

for _ in range(n):
    x, y = input("나이와 이름을 순서대로 작성하시오:").split()
    member_list.append((int(x),y))
    
sorted_list = sorted(member_list, key = lambda x : x[0])

for i in sorted_list:
    print(i[0], i[1])
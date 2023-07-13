data = {
        "a" : 10,
        "b" : 2,
        "c" : 4,
        "d" : 15,
        "e" : 7
}

print("정렬된 값들:")
sorted_data= sorted(data.values())
print(sorted_data)
print("역정렬된 값들:")
sorted_data_reversed = sorted(data.values(),reverse = True)
print(sorted_data_reversed)
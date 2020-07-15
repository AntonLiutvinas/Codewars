def find_uniq(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list[0] if arr.count(list[0]) == 1 else list[1]
print(find_uniq([1, 1, 2, 1]))
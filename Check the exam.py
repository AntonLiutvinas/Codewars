def check_exam(arr1, arr2):
    total_points = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            total_points += 4
        elif arr1[i] != arr2[i] and arr2[i] != "":
            total_points = total_points - 1
        elif arr2[i] == "":
            total_points += 0
    if total_points < 0:
        return 0
    else:
        return total_points

print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))

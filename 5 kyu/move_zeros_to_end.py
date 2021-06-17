def move_zeros(array):
    i = 0
    while True:
        try:
            array.remove(0)
            i += 1
        except ValueError:
            break
    while i != 0:
        array.append(0)
        i = i - 1
    return array

print(move_zeros([0, 1, 2, 0]))
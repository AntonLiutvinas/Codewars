def find_next_square(square):
    import math
    math = int(math.sqrt(square))
    print(math)
    math1 = math + 1
    if math * math == square:
        return math1 * math1
    elif math * math != square:
        return -1
print(find_next_square(26))

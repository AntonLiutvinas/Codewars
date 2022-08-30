def last_digit(n1, n2):
    if n2 == 0 or n1 == 0:
        return 1
    a = str(n1)
    b = str(n2)
    result = int(a[-3:]) ** int(b[-3:])
    final = str(result) if result != 1 else str(0)
    lo = final[-1]
    return int(lo)
list.append()
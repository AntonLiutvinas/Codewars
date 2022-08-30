def divisors(integer):
    list = []
    string = ""
    for i in range(integer):
        if i != 0 and i != 1 and int(integer) % int(i) == 0:
            list.append(i)
    if len(list) == 0:
        return str(integer) + " is prime"
    else:
        return list

print(divisors(1333))

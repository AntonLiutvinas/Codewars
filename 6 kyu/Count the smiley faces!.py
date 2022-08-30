def count_smileys(arr):
    integer = 0
    for i in arr:
        if i.count(":") == 1 or i.count(";") == 1:
            if i.count(")") or i.count("D"):
                if len(i) == 3 and i[1] == "~" or i[1] == "-":
                    integer += 1
    return integer
print(count_smileys([':D',':~)',';~D',':)']))
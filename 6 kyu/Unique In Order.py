def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    listi = [iterable[0]]
    for i in iterable:
        if len(listi) > 0 and i != listi[-1]:
            listi.append(i)
    return listi
print(unique_in_order([1, 2, 3, 3, 4]))
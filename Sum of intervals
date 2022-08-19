def sum_of_intervals(intervals):
    list_of_num1 = []
    list_of_num2 = []
    def range_formater(tuple):
        x = list(tuple)[0]
        y = list(tuple)[1]
        return range(x, y)
    for i in intervals:
        list_of_num1.append(list(range_formater(i)))
    for i in list_of_num1:
        for u in i:
            if u in list_of_num2:
                pass
            else:
                list_of_num2.append(u)
    return len(list_of_num2)

def get_pins(observed):
    pin_screen1 = ["1", "2", "3"]
    pin_screen2 = ["4", "5", "6"]
    pin_screen3 = ["7", "8", "9"]
    pin_screen4 = ["", "0", ""]
    list_of_digits = []
    neighbours = []
    for i in observed:
        list_of_digits.append(int(i))
    for i in list_of_digits:
        lst = [i]
        if i == 0:
            lst.append(8)
        else:
            if i + 1 < 10:
                if i % 3 != 0:
                    lst.append(i + 1)
            if i - 1 > 0:
                if (i - 1) % 3 != 0:
                    lst.append(i - 1)
            if i + 3 < 10:
                lst.append(i + 3)
            if i - 3 > 0:
                lst.append(i - 3)
            if i == 8:
                lst.append(0)
        #neighbours[i] = lst
        neighbours.append(lst)
    number_list = []
    final_list = []
    for i in neighbours:
        number_list.append(i)
    # def number_iteration(iteration_count):
    #     for i in number_list[iteration_count - iteration_count]:
    #         if iteration_count - 1 == 0:
    #             print(str(i))
    #         else:
    #             number_iteration(iteration_count - 1)
    for i in number_list[0]:
        if len(number_list) == 1:
            final_list.append(str(i))
        else:
            for y in number_list[1]:
                if len(number_list) == 2:
                    final_list.append(str(i) + str(y))
                else:
                    for a in number_list[2]:
                        if len(number_list) == 3:
                            final_list.append(str(i) + str(y) + str(a))
                        else:
                            for b in number_list[3]:
                                if len(number_list) == 4:
                                    final_list.append(str(i) + str(y) + str(a) + str(b))
                                else:
                                    for t in number_list[4]:
                                        if len(number_list) == 5:
                                            final_list.append(str(i) + str(y) + str(a) + str(b) + str(t))
                                        else:
                                            for u in number_list[5]:
                                                if len(number_list) == 6:
                                                    final_list.append(str(i) + str(y) + str(a) + str(b) + str(t) + str(u))
                                                else:
                                                    for w in number_list[6]:
                                                        if len(number_list) == 7:
                                                            final_list.append(str(i) + str(y) + str(a) + str(b) + str(t) + str(u) + str(w))
                                                        else:
                                                            for q in number_list[7]:
                                                                final_list.append(str(i) + str(y) + str(a) + str(b) + str(t) + str(u) + str(w) + str(q))
    #number_iteration(2)
    return final_list

print(get_pins("555"))

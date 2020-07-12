def namelist(names):
    string = []
    some_string = ""
    for list in names:
        for value in list.values():
            string.append(value)
    the_len = len(string)
    if the_len >= 2:
        two_last_names = string[-2] + " & " + string[-1]
    if the_len == 1:
        return string[0]
    elif the_len == 2:
        return two_last_names
    elif the_len >= 3:
        for i in range(the_len):
            if i + 2!= the_len or i + 2 > the_len:
                some_string += string[i]
                some_string += ", "
                string_three = string[-1]
        some_variable = some_string.replace(string_three, "") + two_last_names
        return some_variable.replace(" ,", "")
    return ""
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
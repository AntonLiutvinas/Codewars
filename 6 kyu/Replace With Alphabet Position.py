def alphabet_position(text):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = list(range(1, 27))
    my_dict = {key:value for key, value in zip(letters, numbers)}
    the_text = text.upper()
    return_list = []
    string = ""
    for i in the_text:
        if i in letters:
            return_list.append(str(my_dict.get(i)))
    for y in return_list:
        string += y
        string += ' '
    return string.strip()

print(alphabet_position("tetxt"))
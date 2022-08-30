def hex_string_to_RGB(hex_string):
    rgb = ["r", "g", "b"]
    the_list = []
    string = ""
    hex_code = hex_string[1:]
    dictionary = {"0":0, "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    for i in hex_code.upper():
        string += str(dictionary.get(i))
        string += " "
    the_list.append(int(string.split()[0]) * 16 + int(string.split()[1]))
    the_list.append(int(string.split()[2]) * 16 + int(string.split()[3]))
    the_list.append(int(string.split()[4]) * 16 + int(string.split()[5]))
    dicti = {key:value for key, value in zip(rgb, the_list)}
    return dicti

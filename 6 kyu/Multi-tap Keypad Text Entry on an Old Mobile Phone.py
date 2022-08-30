def presses(phrase):
    count_of_presses = 0
    numbers_of_presses_of_a_letter = {"a": 1, "b": 2, "c": 3, "d": 1, "e": 2, "f": 3, "g": 1, "h": 2, "i": 3, "j": 1,"k": 2,"l": 3,"m": 1,"n": 2,"o": 3,"p": 1,"q": 2,"r": 3,"s": 4,"t": 1,"u": 2,"v": 3,"w": 1,"x": 2,"y": 3,"z": 4," ": 1, "1": 1, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 5, "8": 4, "9": 5, "0": 2, "*": 1, "#": 1}
    for i in phrase.lower():
        try:
            count_of_presses += numbers_of_presses_of_a_letter.get(i)
        except TypeError:
            pass
    return count_of_presses

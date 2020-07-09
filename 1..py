

def spin_words(sentence):
    # Creating the function that reverse a string:
    def reversed_string(string):

        list = []
        the_string = ""
        # Adding letters to a list(sorted in a descending order):
        for i in string:
            list.insert(0, i)
        # Concatenating all the letters in to string:
        for i in list:
            the_string += i
        return the_string

    return_string = ""
    split_sentence = sentence.split()
    how_many_words_are_in_sentence = len(split_sentence)
    y = 0
    for i in range(how_many_words_are_in_sentence):
        # Counting how many letters are in word:
        len1 = len(split_sentence[y])
        # If it is more than five, than word is reversed and added to string
        if len1 >= 5:
            return_string += str(reversed_string(split_sentence[y]))
            return_string += " "
        # Otherwise word is added to the string without reversing it
        elif len1 < 5:
            return_string += split_sentence[y]
            return_string += " "
        y += 1


    return(return_string.strip())


print(spin_words("This is my first solved challenge on Codewars"))

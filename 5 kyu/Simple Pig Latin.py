def pig_it(text):
    list_of_words = text.split()
    list_of_new_words = []
    def word_filter(word):
        alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in alphabet:
            if i in word.upper():
                return True
        return False
    for i in list_of_words:
        if word_filter(i):
            list_of_new_words.append(i.replace(i[0], "", 1) + i[0] + "ay")
        else:
            list_of_new_words.append(i)
    strin = ""
    for i in list_of_new_words:
        strin += i + " "
    return strin.rstrip()

print(pig_it("My pig latin !"))
i = "this"
print(i.replace(i[0], "", 1) + i[0] + "ay")

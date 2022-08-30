def anagrams(word, array):
    lst = [wrd for wrd in array if sorted(wrd) == sorted(word)]
    return lst
print(anagrams("bbaa", ["abab", "baba"]))
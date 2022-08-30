def likes(names):
    lens = len(names)
    if lens < 1:
        return "no one likes this"
    elif lens == 1:
        return names[0] + " likes this"
    elif lens == 2:
        return names[0] + " and " + names[1] + " like this"
    elif lens == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif lens > 3:
        return names[0] + ", " + names[1] + " and " + str(lens - 2) + " others like this"

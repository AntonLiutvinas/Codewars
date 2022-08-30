def rgb(r,g,b):
    import math
    red = r if r > -1 else 0
    green = g if g > -1 else 0
    blue = b if b > -1 else 0
    red = red if red <= 255 else 255
    green = green if green <= 255 else 255
    blue = blue if blue <= 255 else 0
    dictionary = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    return f"{dictionary.get(math.floor(red / 16))}{dictionary.get(math.floor(red % 16))}{dictionary.get(math.floor(green / 16))}{dictionary.get(math.floor(green % 16))}{dictionary.get(math.floor(blue / 16))}{dictionary.get(math.floor(blue % 16))}"

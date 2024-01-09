#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new_string = my_string.translate(str.maketrans({"c": None}))
        string_2 = new_string.translate(str.maketrans({"C": None}))
        return string_2
    return my_string

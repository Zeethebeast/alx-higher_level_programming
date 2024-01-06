#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_functions = dir()
    for i in range(0, len(all_functions)):
        if all_functions[i][:2] != "__":
            print("{:s}".format(all_functions[i]))

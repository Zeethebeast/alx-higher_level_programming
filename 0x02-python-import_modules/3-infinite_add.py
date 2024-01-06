#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    numbers = [int(arg) for arg in sys.argv[1:]]
    total = sum(numbers)

    print("{}".format(total))

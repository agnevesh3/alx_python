def argument(*args):
    if len(args) == 0:
        result = print("0 arguments.")
    elif len(args) == 1:
        result = print("1 argument:")
    else:
        result = print(len(args), "arguments:")

    for index, arg in enumerate(args, start=1):
        print("{}: {}".format(index, arg))

    return args


if __name__ == "__main__":
    import sys

    argument(*sys.argv[1:])

if __name__ == "__main__":
    argument("Hello")
if __name__ == "__main__":
    argument("Hello", "Holberton")
if __name__ == "__main__":
    argument()
if __name__ == "__main__":
    argument(98, "battery", "street")

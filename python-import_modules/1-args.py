def argument(*args):
    for index, arg in enumerate(args, start=1):
        print("{}: {}".format(index, arg))


argument("agnaldo")
argument("luis", "john", "anna")

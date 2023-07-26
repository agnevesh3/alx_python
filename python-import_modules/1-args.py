if __name__ == "__main__":

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


argument("edurdo", "costa")

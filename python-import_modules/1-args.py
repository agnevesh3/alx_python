if __name__ == "__main__":

    def argument(*args):
        for index, arg in enumerate(args, start=1):
            print("{}: {}".format(index, arg))

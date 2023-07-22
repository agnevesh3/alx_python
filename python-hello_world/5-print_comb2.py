##00-99
i = -1
while i < 99:
    i = i + 1
    number = "{:02d}".format(i)

    if i == 99:
        print(number)
    else:
        print(number, end=", ")
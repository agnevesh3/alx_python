##Inveting is combination of brains and materials.The more brains you use, the less material you need

for i in range(0, 10):
    for j in range(0, 10):
        if i != j and i < j:
            if i == 8:
                print("{}{}".format((i), (j)))
            else:
                print("{}{}".format((i), (j)), end=", ")

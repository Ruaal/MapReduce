def reduce(file):
    list = open(file, "r")
    for item in list:
        result = 0
        for i in item[1]:
            result+= 1
        pair = (item[0], result)
        output.append(pair)
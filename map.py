def splitting (file, threads):
    text = open(file, "r")
    #Agrupem el text en 5 paquets (1 per thread)
    files = list
    path = "SplitFile"
    for i in range(threads):
        finalpath = path + i
        f = open(finalpath, "w")
        files.append(f)

    #for line, i in text, range(threads):
    for i in range(threads):
        files[i].write(line + "\n")
        if i == (threads - 1):
            i = 0
    for i in range(threads):
        files[i].close()
    text.close()

def mapping(list, name):
    path = "MapFile" + name
    file = open(path, "w")
    for line in list:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            file.write(word + "\n")
    file.close()


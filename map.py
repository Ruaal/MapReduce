THREADS = 4


def splitting(file):
    text = open(file, "r")
    # Agrupem el text en 4 paquets (1 per thread)
    files = []
    path = "splitFile"
    for i in range(THREADS):
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "w")
        files.append(f)
    i = 0
    for line in text:
        files[i].write(line)
        i += 1
        if i == (THREADS):
            i = 0
    for i in range(THREADS):
        files[i].close()
    text.close()


def mapping(idThread):
    entry = open(("splitFile" + str(idThread) + '.txt'), "r")
    path = "mapFile" + str(idThread) + '.txt'
    out = open(path, "w")
    for line in entry:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            out.write(word + "\n")
    out.close()
    entry.close()

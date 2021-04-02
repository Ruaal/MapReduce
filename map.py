from TextCounter import THREADS

def splitting (file):
    text = open(file, "r")
    #Agrupem el text en 5 paquets (1 per thread)
    files = list
    path = "splitFile"
    for i in range(THREADS):
        finalpath = path + i
        f = open(finalpath, "w")
        files.append(f)

    for line, i in text, range(THREADS):
        files[i].write(line + "\n")
        if i == (THREADS - 1):
            i = 0
    for i in range(THREADS):
        files[i].close()
    text.close()
    return files

def mapping(idThread):
    entry = open(("SplitFile" + idThread), "r")
    path = "mapFile" + idThread
    out = open(path, "w")
    for line in entry:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            out.write(word + "\n")
    out.close()
    entry.close()


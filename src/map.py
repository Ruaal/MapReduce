THREADS = 2


def splitting(file):
    text = open(file, "r", encoding='utf8')
    print(text.name + ":")
    # Agrupem el text en 4 paquets (1 per thread)
    files = []
    path = "splitFile"
    for i in range(THREADS):
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "w", encoding='utf8')
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
    entry = open(("splitFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    path = "mapFile" + str(idThread) + '.txt'
    out = open(path, "w", encoding='utf8')
    for line in entry:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            word = word.replace('.', '')
            word = word.replace(',', '')
            word = word.replace(';', '')
            word = word.replace(' ', '')
            out.write(word + "\n")
    out.close()
    entry.close()
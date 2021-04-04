THREADS = 2

def reduce(idThread):
    file = open(("shuffleFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    wordCount = {}
    i = 0
    for word in sorted(file):

        word = word.rstrip("\n")
        if word in wordCount:
            wordCount[word] = wordCount.get(word) + 1
        else:
            wordCount[word] = 1
        if i >= 1000:
            for key, value in wordCount.items():
                print(str(key) + " : " + str(value))
            wordCount.clear()
    for key, value in wordCount.items():
        print(str(key) + " : " + str(value))
    file.close()


def shuffle(idThread):
    items = open(("mapFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    files = []
    path = "shuffleFile"
    for i in range(THREADS):
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "a+", encoding='utf8')
        files.append(f)
    for word in items:
        letter = ord(word[0]) - 97
        i = int(letter % THREADS)
        if i > (THREADS - 1):
            i = THREADS - 1
        files[i].write(word)
    for i in range(THREADS):
        files[i].close()
    items.close()



# La idea seria crear n arxius i que cada thread escrigui en aquests arxius segons la lletra del abecedari rollo
# un modul de 26, hauriem de crear uns semafors per que hi hagues inconscistencia

# Podriem utilitzar el codi ascii per fer el modul (97-122 = a-z)

# Hem de passar totes les lletres a lowercase en algun moment, sigui al principi o al final, ens estalviaria feina
# pel codi ascii

THREADS = 4


def reduce(id_thread):  # conta la cantitat de paraules iguals que hi ha en el fitxer
    file = open(("shuffleFile" + str(id_thread) + '.txt'), "r", encoding='utf8')
    word_count = {}
    for word in file:
        word = word.rstrip("\n")
        if word in word_count:
            word_count[word] = word_count.get(word) + 1
        else:
            word_count[word] = 1

    for key, value in word_count.items():
        print(str(key) + " : " + str(value))

    file.close()


def shuffle(id_thread):  # Assigna a cada fitxer un rang de lletres del alfabet i se li afegeixen les paraules que
    # comencin per aquesta lletra. El rang es calcula amb el modul del numero de threads.
    items = open(("mapFile" + str(id_thread) + '.txt'), "r", encoding='utf8')
    files = []
    path = "shuffleFile"
    for i in range(THREADS):
        final_path = path + str(i) + '.txt'
        f = open(final_path, "a+", encoding='utf8')
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

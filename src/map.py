THREADS = 4


def splitting(file):
    text = open(file, "r", encoding='utf8')
    print(text.name + ":")
    # Agrupem el fitxer en paquets 1 per thread
    files = []  # Creem un array per guardar els file descriptors
    path = "splitFile"
    for i in range(THREADS):  # Creem els fitxers que necessitarem (1 per thread) en mode escritura
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "w", encoding='utf8')
        files.append(f)
    i = 0
    for line in text:
        # Assignem 1 linea a 1 fitxer per cada iteració, el valor i marca el fitxer
        # al que escriure la linea.
        files[i].write(line)
        i += 1
        if i == THREADS:  # Al arribar al ultim fitxer tornem a començar pel primer fitxer
            i = 0
    for i in range(THREADS):
        files[i].close()
    text.close()


def mapping(id_thread):  # Separa les lineas en paraules i elimina espais i alguns caracters especials
    entry = open(("splitFile" + str(id_thread) + '.txt'), "r", encoding='utf8')
    path = "mapFile" + str(id_thread) + '.txt'
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

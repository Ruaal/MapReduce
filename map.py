THREADS = 5
import threading

def splitting (file):
    text = open(file, "r")
    #Agrupem el text en 5 paquets (1 per thread)
    for line, i in text, range(THREADS):
        listoflists[i].append(line)
        if i == (THREADS - 1):
            i = 0
    #si fa out of memory es podria fer el split en txt en comptes de llistes i llavors fer el mapping dels txt
    #TODO: guardar aquests paquets a fitxers separats
    for list in listoflists:
        x = threading.thread(mapping, list)
        threadlist.append(x)

    for thread in threading:
        thread.start()


def mapping(list):
    for line in list:
        line = line.strip()
        words = line.split()
        for word in words:
            print(word, 1)
            #Tenim dos opcions, posar el que pasem al print a una llista de tuples (paraula, 1) o guardar-ho en un fitxer intermig
            #TODO: guardar el resultat en fitxers separats

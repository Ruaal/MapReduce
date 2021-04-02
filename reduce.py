from multiprocessing import Lock
from main import THREADS
def reduce(lock, idThread):
    file = open(("shuffleFile" + idThread), "r")
    result = open("result", "w")
    file.sort()
    aux = None
    for word in file:
        count = 1
        if word == aux:
            count += 1
        else:
            pair = (word + " : " + count + "\n")
            lock.acquire()
            result.write(pair)
            lock.release()
    file.close()
    result.close()
def shuffle(lock, idThread):
    items = open(("MapFile" + idThread), "r")
    files = list
    path = "shuffleFile"
    for i in range(THREADS):
        finalpath = path + i
        f = open(finalpath, "w")
        files.append(f)
    for word in items:
        letter = ord(word[0]) - 97
        i = int(letter/THREADS)
        if i > (THREADS - 1):
            i = THREADS - 1
        lock.acquire()
        files[i].write(word + "\n")
        lock.release()
    for i in range(THREADS):
        files[i].close()

    items.close()


#La idea seria crear n arxius i que cada thread escrigui en aquests arxius segons la lletra del abecedari rollo
#un modul de 26, hauriem de crear uns semafors per que hi hagues inconscistencia

#Podriem utilitzar el codi ascii per fer el modul (97-122 = a-z)

#Hem de passar totes les lletres a lowercase en algun moment, sigui al principi o al final, ens estalviaria feina
#pel codi ascii
def reduce(file):
    list = open(file, "r")
    result = open("result", "r")
    list.sort()
    aux = None
    for item in list:
        count = 1
        if item == aux:
            count += 1
        else:
            pair = (item + " : " + count + "\n")
            result.write(pair)

def shuffle(file, numthreads):
    items = open(file, "r")
    files = list
    path = "shuffleFile"
    for i in range(numthreads):
        finalpath = path + i
        f = open(finalpath, "w")
        files.append(f)
    for word in items:
        letter = ord(word[0]) - 97
        i = int(letter/numthreads)
        if i > (numthreads - 1):
            i = numthreads - 1
        files[i].write(word + "\n")
    for i in range(numthreads):
        files[i].close()

    items.close()


#La idea seria crear n arxius i que cada thread escrigui en aquests arxius segons la lletra del abecedari rollo
#un modul de 26, hauriem de crear uns semafors per que hi hagues inconscistencia

#Podriem utilitzar el codi ascii per fer el modul (97-122 = a-z)

#Hem de passar totes les lletres a lowercase en algun moment, sigui al principi o al final, ens estalviaria feina
#pel codi ascii
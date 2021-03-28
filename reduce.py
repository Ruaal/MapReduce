def reduce(file):
    list = open(file, "r")
    for item in list:
        result = 0
        for i in item[1]:
            result+= 1
        pair = (item[0], result)
        output.append(pair)

def shuffle(file, numthreads):
    items = open(file, "r")


#La idea seria crear n arxius i que cada thread escrigui en aquests arxius segons la lletra del abecedari rollo
#un modul de 26, hauriem de crear uns semafors per que hi hagues inconscistencia

#Podriem utilitzar el codi ascii per fer el modul (97-122 = a-z)

#Hem de passar totes les lletres a lowercase en algun moment, sigui al principi o al final, ens estalviaria feina
#pel codi ascii
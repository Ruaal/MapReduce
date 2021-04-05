__author__ = "Joan Ruiz, David Aguilera"
from multiprocessing import Pool  # Pool permet la paral·lelització dels threads
import sys  # Sys permet llegir els arguments passats per linea de comanda
import os  # Os permet borrar els fitxers temporals creats
from src import map, reduce

THREADS = 4
''' La constant THREADS ens permetra decidir la cantitat de processos paral·lels que volem alhora
 Per evitar importacions cicliques aquesta es declarara a cada fitxer (tambè es podria crear un fitxer nomes per
 aquesta constant '''


def main():
    for file in sys.argv[1:]:
        # Per cada fitxer a la linea de comanda fem les fases del algorisme, on split es sempre seqüencial i els altres
        # Es faran amb una pool de n threads
        map.splitting(file)
        pool = Pool(THREADS)
        pool.map(map.mapping, range(THREADS))
        pool.close()
        pool.join()
        pool = Pool(THREADS)
        pool.map(reduce.shuffle, range(THREADS))
        pool.close()
        pool.join()
        pool = Pool(THREADS)
        pool.map(reduce.reduce, range(THREADS))
        pool.close()
        pool.join()

        for i in range(THREADS):  # Borrem els fitxers temporals creats
            os.remove("mapFile" + str(i) + '.txt')
            os.remove("shuffleFile" + str(i) + '.txt')
            os.remove("splitFile" + str(i) + '.txt')


if __name__ == '__main__':
    main()

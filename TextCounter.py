from multiprocessing import Pool
import sys
import os
from src import map, reduce

THREADS = 2


def main():
    for file in sys.argv[1:]:
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

        # for i in range(THREADS):
    # os.remove("mapFile" + str(i) + '.txt')
    # os.remove("shuffleFile" + str(i) + '.txt')
    # os.remove("splitFile" + str(i) + '.txt')


if __name__ == '__main__':
    main()

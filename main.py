THREADS = 4
from multiprocessing import Pool, Lock
import map
import reduce
import sys

for file in sys.argv:
    with Pool(THREADS) as pool:
        pool.map(map.splitting(file, THREADS))
    map.splitting(file, THREADS)
    map.mapping(file
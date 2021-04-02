THREADS = 4
from functools import partial
from multiprocessing import Pool, Manager
import map
import reduce
import sys

for file in sys.argv:
    map.splitting(file)
    with Manager() as manager, manager.Lock() as lock, Pool(THREADS) as pool:
        pool.map(map.mapping ,range(THREADS))
        shuffleLocked = partial(reduce.shuffle, lock)
        pool.map(shuffleLocked, range(THREADS))
        reduceLocked = partial(reduce.reduce, lock)
        pool.map(reduceLocked, range(THREADS))
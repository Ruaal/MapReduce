from multiprocessing import Pool, Lock
import sys
import os

THREADS = 4
lock = Lock()

def splitting(file):
    text = open(file, "r", encoding='utf8')
    # Agrupem el text en 4 paquets (1 per thread)
    files = []
    path = "splitFile"
    for i in range(THREADS):
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "w", encoding='utf8')
        files.append(f)
    i = 0
    for line in text:
        files[i].write(line)
        i += 1
        if i == (THREADS):
            i = 0
    for i in range(THREADS):
        files[i].close()
    text.close()


def mapping(idThread):
    entry = open(("splitFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    path = "mapFile" + str(idThread) + '.txt'
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




def reduce(idThread):
    global lock
    file = open(("shuffleFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    wordCount = {}
    i = 0
    for word in sorted(file):

        word = word.rstrip("\n")
        if word in wordCount:
            wordCount[word] = wordCount.get(word) + 1
        else:
            wordCount[word] = 1
        if i >= 1000:
            lock.acquire()
            for key, value in wordCount.items():
                print(str(key) + " : " + str(value))
            lock.release()
            wordCount.clear()
    lock.acquire()
    for key, value in wordCount.items():
        print(str(key) + " : " + str(value))
    lock.release()
    file.close()


def shuffle(idThread):
    global lock
    items = open(("mapFile" + str(idThread) + '.txt'), "r", encoding='utf8')
    files = []
    path = "shuffleFile"
    for i in range(THREADS):
        finalpath = path + str(i) + '.txt'
        f = open(finalpath, "a+", encoding='utf8')
        files.append(f)
    for word in items:
        letter = ord(word[0]) - 97
        i = int(letter / THREADS)
        if i > (THREADS - 1):
            i = THREADS - 1
        lock.acquire()
        files[i].write(word)
        lock.release()
    for i in range(THREADS):
        files[i].close()
    items.close()


def main():
    for file in sys.argv[1:]:
        splitting(file)
        pool = Pool(THREADS)
        pool.map_async(mapping, range(THREADS))
        pool.close()
        pool.join()
        pool = Pool(THREADS)
        pool.map_async(shuffle, range(THREADS))
        pool.close()
        pool.join()
        pool = Pool(THREADS)
        pool.map_async(reduce, range(THREADS))
        pool.close()
        pool.join()
        
        for i in range(THREADS):
        	os.remove("mapFile" + str(i) + '.txt')
        	os.remove("shuffleFile" + str(i) + '.txt')
        	os.remove("splitFile" + str(i) + '.txt')


if __name__ == '__main__':
    main()

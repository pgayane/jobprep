import random
import string
from nativeHT import NaiveHT
from listHT import listHT
from sortedlistHT import sortedlistHT
import time

def test_listHt():
    lt = listHT()

    for key in string.ascii_letters:
        lt.put(key, random.randint(1, 100))


    print lt

    print lt.get('ab')
    print lt.get('b')

    lt.remove('b')
    print lt.get('b')

    print lt


# testing sortedlistHT
def test_sortedlistHT():
    lt = sortedlistHT()

    for i in range(10, 0, -1):
        lt.put(i, random.randint(1, 100))


    print lt

    print lt.get(3)
    print lt.get(11)

    lt.remove(3)
    print lt.get(3)

    print lt

def test_performance():
    nHT = NaiveHT()
    lt = listHT()
    sHT = sortedlistHT()

    keys =  [i for i in range(10000)]
    
    random.shuffle(keys)

    for key in keys:
        v = random.randint(1, 100)
        nHT.put(key, v)
        lt.put(key, v)
        sHT.put(key, v)

    now = time.time()
    
    c = 0
    random.shuffle(keys)
    while(time.time() - now < 0.1):
        nHT.get(keys[c%10000])
        c += 1
    print 'native data structure: ' + str(c)

    now = time.time()
    c = 0
    while(time.time() - now < 0.1):
        lt.get(keys[c%10000])
        c += 1
    print 'list data structure: ' + str(c)

    now = time.time()
    c = 0
    while(time.time() - now < 0.1):
        sHT.get(keys[c%10000])
        c += 1
    print 'sorted list data structure: ' + str(c)


if  __name__ =='__main__':
    test_performance()
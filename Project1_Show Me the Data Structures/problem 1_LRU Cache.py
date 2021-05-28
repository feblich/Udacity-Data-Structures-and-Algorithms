
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        if capacity is None:
            raise ValueError("capacity value must not be None")
        if capacity < 1:
            raise ValueError("capacity value must be greater than 1")
        self.capacity = capacity
        self.ordereddict = OrderedDict()

    def get(self, key):

        if key not in self.ordereddict:
            return -1

        self.ordereddict.move_to_end(key)
        return self.ordereddict[key]

    def set(self, key, value):

        if key in self.ordereddict:
            self.ordereddict.move_to_end(key)
        self.ordereddict[key] = value

        if len(self.ordereddict) > self.capacity:
            self.ordereddict.popitem(last=False)


if __name__ == '__main__':

    # test case 1, length 5
    our_cache = LRUCache(5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # test case 2, length n = 100
    n = 100
    keys = list(range(n+5))
    our_cache = LRUCache(n)
    for k in keys:
        our_cache.set(k, k)

    print(our_cache.get(0)) # must return -1 because 0 is discarded as a LRU element when cache hit limit n=100
    print(our_cache.get(1)) # must return -1 because 1 is discarded as a LRU element when cache hit limit n=100
    print(our_cache.get(2)) # must return -1 because 2 is discarded as a LRU element when cache hit limit n=100
    print(our_cache.get(3)) # must return -1 because 3 is discarded as a LRU element when cache hit limit n=100
    print(our_cache.get(4)) # must return -1 because 4 is discarded as a LRU element when cache hit limit n=100
    print(our_cache.get(5)) # must return 5 because 5 is the 6th element added to the cache and is still in


    # edge case 1, None capacity
    try:
        our_cache = LRUCache(None) # must raise exception: 'capacity value must not be None'
    except ValueError as v:
        print(v)

    try:
        our_cache = LRUCache(0) # must raise exception: 'capacity value must be greater than 1'
    except ValueError as v:
        print(v)

    try:
        our_cache = LRUCache(-1) # must raise exception: 'capacity value must be greater than 1'
    except ValueError as v:
        print(v)


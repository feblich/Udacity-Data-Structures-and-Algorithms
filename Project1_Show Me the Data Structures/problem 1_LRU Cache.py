
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):

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
    our_cache = LRUCache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    our_cache.get(1)  # returns 1
    our_cache.get(2)  # returns 2
    our_cache.get(9)  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

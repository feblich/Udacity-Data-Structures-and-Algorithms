
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
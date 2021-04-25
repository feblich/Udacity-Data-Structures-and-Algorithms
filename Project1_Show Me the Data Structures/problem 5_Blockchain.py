import time
import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.tail = None

    def size(self):

        size = 0
        current_tail = self.tail
        while current_tail:
            size += 1
            current_tail = current_tail.previous_hash
        return size

    def append(self, data):

        if self.tail:
            new_block = Block(data=data, previous_hash=self.tail)
            self.tail = new_block
            return

        new_block = Block(data=data, previous_hash=None)
        self.tail = new_block


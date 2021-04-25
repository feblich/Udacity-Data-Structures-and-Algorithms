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

    def get_block_location(self, data):

        if self.tail.data == data:
            location = self.size()
            return location, data

        current_tail = self.tail
        current_loc = self.size()
        while current_tail:
            if current_tail.data != data:
                current_loc -= 1
                if current_loc == 0:
                    return None
                current_tail = current_tail.previous_hash
            else:
                return current_loc, data


# testing
if __name__ == '__main__':

    blockchain = Blockchain()
    print(blockchain.size())  # must be 0

    blockchain.append('data0')
    blockchain.append('data1')
    blockchain.append('data2')
    blockchain.append('data3')

    print(blockchain.size())  # must be 4
    print(blockchain.tail.data)  # must be 'data3'
    print(blockchain.get_block_location('data1'))  # must return (2, 'data1') which is location of this block







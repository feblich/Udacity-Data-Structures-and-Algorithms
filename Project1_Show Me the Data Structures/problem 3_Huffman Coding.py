import sys
from operator import itemgetter


class Element:
    def __init__(self, character=None, frequency=0):

        self.character = character
        self.frequency = frequency


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

class Node(object):

    def __init__(self, left_child=None, left_freq=0, right_child=None, right_freq=0, letter=None):

        self.left_child = left_child
        self.right_child = right_child
        self.letter = letter
        self.frequency = left_freq + right_freq

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":

    s = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    d = {}
    list_of_nodes = []
    letters = ''.join(set(s))
    for l in letters:
        d[l] = s.count(l)

    two_mins = sorted(d.items(), key=itemgetter(1))[:2]

    # node = Node(left_child=two_mins[0][0], left_freq=two_mins[0][1], right_child=two_mins[1][0],
    #             right_freq=two_mins[1][1])

    node = Node(left_child=Node(letter=two_mins[0][0], left_freq=two_mins[0][1]), left_freq=two_mins[0][1],
                right_child=Node(letter=two_mins[1][0], right_freq=two_mins[1][1]), right_freq=two_mins[1][1])
    del d[two_mins[0][0]]
    del d[two_mins[1][0]]
    # d[node] = node.value
    d[node] = node.frequency
    list_of_nodes.append(node)
    while len(d) >= 2:

        two_mins = sorted(d.items(), key=itemgetter(1))[:2]

        new_node = Node(left_child=two_mins[0][0], left_freq=two_mins[0][1], right_child=two_mins[1][0],
                        right_freq=two_mins[1][1])

        del d[two_mins[0][0]]
        del d[two_mins[1][0]]
        d[new_node] = new_node.frequency

        # if node.value <= new_node.value:
        #     new_node.set_right_child(node)
        # else:
        #     new_node.set_left_child(node)
        #
        list_of_nodes.append(new_node)

huffman_tree = list_of_nodes[-1]

def get_letter_code(node):
    from collections import defaultdict
    huff_code = Stack()
    letter_codes = defaultdict(list)
    if node.left_child:
        if node.left_child.letter:
            huff_code.push(0)
            letter_codes[node.left_child.letter] = huff_code.items
            huff_code.pop()
            if node.right_child.letter:
                huff_code.push(1)
                letter_codes[node.right_child.letter] = huff_code.items

        get_letter_code(node.left_child)

    return huff_code



get_letter_code(huffman_tree)
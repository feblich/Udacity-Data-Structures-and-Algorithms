import sys
from operator import itemgetter
from collections import defaultdict

class Node(object):

    def __init__(self, left_child=None, right_child=None, freq=0, letter=None):

        self.left_child = left_child
        self.right_child = right_child
        self.letter = letter
        self.freq = freq
        self.huff_binary = ''

def get_huffman_tree(the_string):
    d = {}
    letters = ''.join(set(the_string))
    for l in letters:
        d[l] = the_string.count(l)

    nodes = [Node(freq=v, letter=k) for k, v in
             d.items()]  # create a list of nodes, leaf nodes lef and right children are None

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda
            x: x.freq)  # sort nodes based on freq so index 0 and 1 can be chosen as left and right child
        left_child = nodes[0]
        right_child = nodes[1]
        left_child.huff_binary = 0
        right_child.huff_binary = 1
        new_node = Node(left_child=left_child, right_child=right_child, freq=left_child.freq + right_child.freq,
                        letter=left_child.letter + right_child.letter)
        nodes.remove(left_child)
        nodes.remove(right_child)
        nodes.append(new_node)

    return nodes[0]

def traverse_huffman_tree(huffman_tree, val='', letter_codes=defaultdict(list)):

    huff_code = val + str(huffman_tree.huff_binary)
    if huffman_tree.left_child:
        traverse_huffman_tree(huffman_tree.left_child, huff_code)
    if huffman_tree.right_child:
        traverse_huffman_tree(huffman_tree.right_child, huff_code)

    if huffman_tree.left_child is None and huffman_tree.right_child is None:
        letter_codes[huffman_tree.letter] = huff_code

    return letter_codes

def huffman_encoding(data):
    huffman_tree = get_huffman_tree(data)
    huff_codes_dict = traverse_huffman_tree(huffman_tree)
    encoded_data = ''
    for letter in data:
        encoded_data += huff_codes_dict[letter]

    return encoded_data, huffman_tree





def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":

    s = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    encoded_data, tree = huffman_encoding(s)

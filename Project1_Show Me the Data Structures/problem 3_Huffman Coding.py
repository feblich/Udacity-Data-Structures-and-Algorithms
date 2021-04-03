import sys
from operator import itemgetter


class Element:
    def __init__(self, character=None, frequency=0):

        self.character = character
        self.frequency = frequency

class Node(object):

    def __init__(self, left_child=None, left_freq=0, right_child=None, right_freq=0):

        self.left_child = left_child
        self.right_child = right_child
        self.value = left_freq + right_freq


def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    # codes = {}
    #
    # a_great_sentence = "The bird is the word"
    #
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))
    #
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    s = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    d = {}
    list_of_nodes = []
    letters = ''.join(set(s))
    for l in letters:
        d[l] = s.count(l)

    two_mins = sorted(d.items(), key=itemgetter(1))[:2]
    # el1 = Element(two_mins[0][0], two_mins[0][1])
    # el2 = Element(two_mins[1][0], two_mins[1][1])
    # node = Node(el1, el2)
    node = Node(left_child=two_mins[0], left_freq=two_mins[0][1], right_child=two_mins[1],
                right_freq=two_mins[1][1])

    del d[two_mins[0][0]]
    del d[two_mins[1][0]]
    d[node] = node.value

    list_of_nodes.append(node)
    while len(d) >= 2:

        two_mins = sorted(d.items(), key=itemgetter(1))[:2]
        new_node = Node(left_child=two_mins[0], left_freq=two_mins[0][1], right_child=two_mins[1],
                right_freq=two_mins[1][1])

        del d[two_mins[0][0]]
        del d[two_mins[1][0]]
        d[new_node] = new_node.value

        # if node.value <= new_node.value:
        #     new_node.set_right_child(node)
        # else:
        #     new_node.set_left_child(node)
        #
        list_of_nodes.append(new_node)

from collections import defaultdict
encoded_dict = defaultdict(str)

huffman_tree = list_of_nodes[-1]
left_child = huffman_tree.left_child

while type(left_child) is tuple and type(left_child[0]) is not str:
    left_child = left_child[0].left_child
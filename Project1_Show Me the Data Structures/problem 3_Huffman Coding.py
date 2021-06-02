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
            x: (x.freq, x.letter))  # sort nodes based on freq so index 0 and 1 can be chosen as left and right child

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
    if not data:
        raise ValueError("input sentence should not be empty")
    huffman_tree = get_huffman_tree(data)
    huff_codes_dict = traverse_huffman_tree(huffman_tree)
    encoded_data = ''
    for letter in data:
        encoded_data += huff_codes_dict[letter]

    return encoded_data, huffman_tree


def huffman_decoding(encoded_data,tree):

    decoded_data = ''
    curr_tree = tree
    for bit in encoded_data:

        if bit == str(0):
            curr_tree = curr_tree.left_child

        if bit == str(1):
            curr_tree = curr_tree.right_child

        if curr_tree.left_child is None and curr_tree.right_child is None:
            decoded_data += curr_tree.letter
            curr_tree = tree

    return decoded_data



if __name__ == "__main__":

    ## test with "AAAAAAABBBCCCCCCCDDEEEEEE"
    s = "AAAAAAABBBCCCCCCCDDEEEEEE"
    encoded_data, huffman_tree = huffman_encoding(s)
    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(decoded_data)  # "AAAAAAABBBCCCCCCCDDEEEEEE"

    ## test with another sentence "The bird is the word"
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1110000100011011101010100111111001001111101010001000110101101101001111

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word


    ## edge case 1 (multiple spaces) "Sentence with     multiple spaces"
    multiple_space_sentence = "Sentence with     multiple spaces"
    print("The size of the data is: {}\n".format(sys.getsizeof(multiple_space_sentence)))
    # The size of the data is: 82
    print("The content of the data is: {}\n".format(multiple_space_sentence))
    # The content of the data is: Sentence with     multiple spaces

    encoded_data, tree = huffman_encoding(multiple_space_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 40
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 01000110100111111101001010111000111010111111101100000000000001101111001000111101111010100011000101110100100101011101011

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 82
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: Sentence with     multiple spaces


    ## edge case 2 (empty sentence) ""
    empty_sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
    # The size of the data is: 51
    print("The content of the data is: {}\n".format(empty_sentence))
    # The content of the data is:
    try:
        encoded_data, tree = huffman_encoding(empty_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
    except ValueError as v:
        print(v)
        # input sentence should not be empty





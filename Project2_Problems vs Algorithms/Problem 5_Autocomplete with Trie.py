## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        if len(self.children) == 0:
            return results

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        for char in self.children:
            results.extend(self.children[char].suffixes(suffix=suffix + char))

        return results


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        curr_node = self.root

        for char in word:
            curr_node.insert(char)
            curr_node = curr_node.children[char]

        curr_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node




# testing
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find('f').suffixes())
print(MyTrie.find('ant').suffixes())
print(MyTrie.find('tri').suffixes())

# Reference: https://github.com/Axel-Bravo/19_udacity_dsa/blob/master/3_003_Project_Problems_vs_Algorithms/005_Problem_5.py
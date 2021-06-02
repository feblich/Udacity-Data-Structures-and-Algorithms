
# Writeups

## problem 1 LRU Cache

An LRU cache should have a mechanism to keep track of the priority of items in terms of the frequency that they have
been used and if a new item is added to the cach the item with the has been least recently called must be discarded.
In order to construct this data structure, I used `OrderedDict()` function from collections library which combines both
a hash map and a linked list. the get method would use move_to_end method of `OrderedDict()` to move the requested item's key to the end of the cache.
The set method, would add/move the requested item to the end of the cache and if length of cache object, as a result of
this operation becomes greater than capacity, it will pop the first item in the cache.
Both get and set methods are in O(1) time because `move_to_end` and `popitem` methods of `OrderedDict()` are done in constant time.


## problem 2 File Recursion

Since there is no limit to the depth of the subdirectories, recursion could be a good approach to solve this problem.
In this approach, for each object in the folder, if object is a subdirectory, `find_files` function is called recursively
to get all files in subdirectories below the folder until all files in all subdirectories are extracted. Only files with
suffix .c are selected. Time complexity depends on depth of the subdirectories and the number of files in each, therefore
it approximately has O(depth*number of files in the folder)

## problem 3 Huffman Coding

In my implementation, the Huffman tree for a string of characters is consisted of node objects. Each node object has the
following attributes:
- `left_child` which is a node object itself
- `right_child` which is a node object itself
- `freq` which is the sum of left and right node frequencies
- `letter`
- `huff_binary` which demonstrates whether the node is on the left(0) or right(1) of its parent

I then constructed the Huffman tree by creating a list of leaf nodes (nodes where `left_child` and `right_child` are `None`)
and merging the 2 nodes with the lowest frequency and resorting the list until only one node (the Huffman tree) is left.
I then traverse the Huffman tree recursively to generate a dictionary of letters with their corresponding Huffman code.
This dictionary is used to generate Huffman encoding for a given string. Given a Huffman tree and the encoded string, I
can decode by going left (when encountered 0) and right (when encountered 1) in the tree until a leaf node is reached,
after which I need to go back to the root of the tree and repeat until all bits in the encoded string are traversed.
Traversing list of nodes takes O(n) time where n is the length of the list so time complexity highly depends on the size
of the input string. The sorted function used to sort list of nodes has O(n log(n)) time complexity.

## problem 4 Active Directory

Because there is no definitive limit to the size of the group, recursion would be a good choice to look for a user in
the group. `is_user_in_group(user,group)` function is recursively called for each subgroup in group to check for existence of `user`
Time complexity depends on the number of users and structure of the group, therefore it approximately has
O(number of users * structure of the group).

## problem 5 Blockchain

The blockchain data structure has similarities with a linked list as it is consisted of sequential but non-contiguous data
elements that point to each other. However there are some differences, as the blockchain is traversed backwards and also
elements cannot be changed, i.e. they are immutable. `append` has time O(1) since we only append to tail, but `size` and
`get_block_location` require traversal of the blockchain and therefore depend on the size O(n)

## problem 6 Union and Intersection

For this problem, first, values of linked list nodes for both linked list objects must be extracted into a list. And
subsequently union and intersection operations are performed on these unique values. I think current implementation of 
union and intersection both take O(n)
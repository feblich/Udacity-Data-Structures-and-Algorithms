
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
In this approach, for each object in the folder, if object is a subdirectory, find_files function is called recursively
to get all files in subdirectories below the folder until all files in all subdirectories are extracted. Only files with
suffix .c are selected. Time complexity depends on depth of the subdirectories and the number of files in each.

## problem 3 Huffman Coding

I was able to create the Huffman tree by creating a dictionary of letters and their frequency and then replacing couple
of elements from this dictionary with lowest frequency with node object. Now th task is to extract huffman coding
by traversing from a letter node at the bottom of the tree to the top node which can be done with a stack.

## problem 4 Active Directory

Because there is no definitive limit to the size of the group, recursion would be a good choice to look for a user in
the group. `is_user_in_group(user,group)` function is recursively called for each subgroup in group to check for existence of `user`
Time complexity depends on the number of users and structure of the group.

## problem 5 Blockchain

The blockchain data structure has similarities with a linked list as it is consisted of sequential but non-contiguous data
elements that point to each other. However there are some differences, as the blockchain is traversed backwards and also
elements cannot be changed, i.e. they are immutable. `append` has time O(1) since we only append to tail, but `size` and
`get_block_location` require traversal of the blockchain and therefore depend on the size O(n)

## problem 6 Union and Intersection

For this problem, first, values of linked list nodes for both linked list objects must be extracted into a list. And
subsequently union and intersection operations are performed on these unique values. I think current implementation of 
union and intersection both take O(n)
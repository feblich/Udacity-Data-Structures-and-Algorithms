# Writeups

## problem 1 square root of an integer

In this question square root function is implemented from scratch. Since the expected time complexity is O(log(n))
a variant of binary search is algorithm is implemented. In this algorithm, it is assumed that there is a sorted array
of natural numbers starting from 1 until the given number. We leverage the fact that the square root of a number
is half or less so we can put a check on this as the midpoint. At each iteration, if the midpoint squared of the array is less
than the given number, we can get rid of the first half of the numbers and continue the search in this new half
and if the mid value square is greater than the given number we can get rid of the half of the array on the righ side
of mid value until mid value square is equal to the number. 

- Time & Space Complexity


Time complexity is O(log(n)) as we traverse the natural number list by a binary search approach. Space complexity is `O(1)`
  as it is independent of the input size.


## problem 2 search in a rotated sorted array

In this problem, the index of the number is found by first recursively locating the pivot point where the list is rotated.
The `find_pivot()` function uses the concept of binary search and finds the pivot point recursively. After this points
is located, it can be used as kind of a midpoint in the `rotated_array_search` to find the index of the requested number
in the list. 

- Time & Space Complexity


Given that both functions are based on binary search algorithm, the time complexity is `O(log(n))`. Similar
to problem 1, space complexity is independent of input size and thus is O(1).

## problem 3 rearrange array elements

The idea behind the algorithm that is used to solve this problem is that in a sorted array (descending), the digit that
is located on the far left of the number is the most important one. Therefore, we should aim to pick the highest value
for the digit on the left of both numbers. The algorithm first sorts the array in descending order (without using Python
sort function and a recursive approach (quicksort)), then 2 numbers are formed using digits on odd and even index locations. 

- Time & Space Complexity


Since quicksort is used for the sorting part, best case time complexity is `O(nlog(n))` and worst time complexity is `O(n2)`. 
source: https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/ 
Space complexity of the quicksort part is `Olog(n)`, source: https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/

## problem 4 Dutch national flag

The algorithm is based on moving on all zeros to the left, and all twos to the right of all ones. This is done by 
moving low, mid and high index of the array by conditioning the values of the array at these index locations. Initially,
the mid index is at 0, if `arr[mid]==1` then the element is not moved and instead mid index is moved to the right. If 
`arr[mid] == 2` it is moved to the right most position and if it is one, to the leftmost position. 

- Time & Space Complexity


Time complexity is`O(n)` because all elements in the array are visited. Space complexity `O(1)` since we are using only
  a few pointers.

## problem 5 autocomplete with Trie

A trie is a tree data structure (not necessarily binary tree) where each node contains a letter (key) and children (value),
and a tag that specifies whether that node denotes a word. The root node does not denote letter but it has children.
Given a letter(s), the tree is traversed to retrieve all valid words that begin with that letter(s). Similar to tree
traversal, trie traversal is done through recursive algorithms. 

- Time & Space Complexity

Time complexity of methods in Trie and TriNode classes are as follows:

- `__init__` method of TrieNode class does not depend on the length of any input object and thus is `O(1)` 
- `__init__` method of Trie class instantiates a TrieNode object in the root of Trie and similar to above, is `O(1)`
- `insert` method in Trie class is `O(n)` where `n` is the length of the word being inserted.
- `insert` method in TrieNode class depends on the length of `char` and since this length is always 1, therefore time complexity is `O(1)`
- `find` method in Trie class is `O(n*s)` where `n` is the length of the word and `s` is the length of search path (nodes visited).
- `suffixes` method in TrieNode is `O(n*s)` where `n` is the number of complete words in the input list and `s` is the length of search path (nodes visited).

Space complexity of methods is Trie and TrieNode classes are as follows:

- `__init__` method of TrieNode class does not depend on the length of any input object and thus is `O(1)` 
- `__init__` method of Trie class instantiates a TrieNode object in the root of Trie and similar to above, is `O(1)`
- `insert` and `find` in Trie class: Space complexity depends on the total number of words in the trie and the worst case happens when there are no common 
characters between the words and therefore we should have a node for each letter, `O(n)` for both **insert and find**
- `insert` method in TrieNode class is `O(1)` as the length of `char` is always 1.
- `suffixes` method in TrieNode class is a recursive function and thus its space complexity is proportional to the max depth of recursion.
Therefore, space complexity for this methods is `O(m*n)` where `m` is the space required for each substring that completes
  the prefix and `n` is the max depth (number of such substrings).

## problem 6 unsorted integer array

In this problem we would like to find min and max of an array in a single traversal. There is no need to sort the array
and the task can be done using two placeholders as reference for max and min values. 

- Time & Space Complexity

Time complexity is `O(n)` where n is the size of the array (there is only one traversal of the array). As we only have 
  two pointers (for max and min, mentioned above), space complexity is independent of array size and thus is `O(1)`

## problem 7 HTTP router with Trie

In the implementation of HTTP router for this exercise we would use a trie data structure with some modifications. Most
notably, instead of splitting the path into letters, we would split the path based on the parts that are separated by 
a `/`. The Router class is made up of a RouterTrie at the root and RouterTrie contains RouterTrieNodes at its root with
associated children. 

- Time & Space Complexity


**Time Complexity**
  

Time complexity of **lookup** and **insertion** depends on the length of the word, `a` that's being searched for or inserted 
and the number of total words `n`, and therefore is `O(a*n)`. The worst case for time complexity is for lookup and
insertion of the longest key from a trie with the most number of keys. If `n` is the number of components
in the path, then space complexity would be `O(n)`.
  

**Space Complexity**


Space complexity for **insertion** and **lookup** is `O(n)` where `n` is the number of components in the path
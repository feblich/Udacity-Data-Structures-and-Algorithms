# Writeups

## problem 1 square root of an integer

In this question square root function is implemented from scratch. Since the expected time complexity is O(log(n))
a variant of binary search is algorithm is implemented. In this algorithm, it is assumed that there is a sorted array
of natural numbers starting from 1 until the given number. We leverage the fact that the square root of a number
is half or less so we can put a check on this as the midpoint. At each iteration, if the midpoint squared of the array is less
than the given number, we can get rid of the first half of the numbers and continue the search in this new half
and if the mid value square is greater than the given number we can get rid of the half of the array on the righ side
of mid value until mid value square is equal to the number. Time complexity is O(log(n)) as we traverse the natural
number list by a binary search approach. Space complexity is O(1) as it is independent of the input size.


## problem 2 search in a rotated sorted array

In this problem, the index of the number is found by first recursively locating the pivot point where the list is rotated.
The `find_pivot()` function uses the concept of binary search and finds the pivot point recursively. After this points
is located, it can be used as kind of a midpoint in the `rotated_array_search` to find the index of the requested number
in the list. Given that both functions are based on binary search algorithm, the time complexity is `O(log(n))`. Similar
to problem 1, space complexity is independent of input size and thus is O(1).

## problem 3 rearrange array elements

The idea behind the algorithm that is used to solve this problem is that in a sorted array (descending), the digit that
is located on the far left of the number is the most important one. Therefore, we should aim to pick the highest digit
for the digit on the left of both numbers. The algorithm first sorts the array in descending order (without using Python
sort function and a recursive approach (quicksort)), then 2 numbers are formed using digits on odd and event index locations. Time
complexity is `O(log(n))` since it is a variation of binary search. Space complexity is independent of input size and 
is `O(1)`.

## problem 4 Dutch national flag

The algorithm is based on moving on all zeros to the left, and all twos to the left of all ones. This is done by 
moving low, mid and high index of the array by conditioning the values of the array at these index locations. Initially,
the mid index is at 0, if `arr[mid]==1` then the element is not moved and instead mid index is moved to the right. If 
`arr[mid] == 2` it is moved to the right most position and if it is one, to the leftmost position. Time complexity is 
`O(n)` because all elements in the array are visited. Space complexity is also `O(n)`.

## problem 5 autocomplete with Trie

A trie is a tree data structure (not necessarily binary tree) where each node contains a letter (key) and children (value),
and a tag that specifies whether that node denotes a word. The root node does not denote letter but it has children.
Given a letter(s), the tree is traversed to retrieve all valid words that begin with that letter(s). Similar to tree
traversal, trie traversal is done through recursive algorithms. Time complexity of search and insert for this implementation,
depends on the length of the word and total number of words in the trie, n, and is `O(word*n)`. Space complexity depends on the
total number of words in the trie and is `O(n)`
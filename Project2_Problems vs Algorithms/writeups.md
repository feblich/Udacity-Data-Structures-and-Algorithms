# Writeups

## problem 1 LRU Cache

In this question square root function is implemented from scratch. Since the expected time complexity is O(log(n))
a variant of binary search is algorithm is implemented. In this algorithm, it is assumed that there is a sorted array
of natural numbers starting from 1 until the given number. We leverage the fact that the square root of a number
is half or less so we can put a check on this as the midpoint. At each iteration, if the midpoint squared of the array is less
than the given number, we can get rid of the first half of the numbers and continue the search in this new half
and if the mid value square is greater than the given number we can get rid of the half of the array on the righ side
of mid value until mid value square is equal to the number. Time complexity is O(log(n)) as we traverse the natural
number list by a binary search approach. Space complexity is O(1) as it is independent of the input size.

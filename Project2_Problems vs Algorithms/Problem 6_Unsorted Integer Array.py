def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
      ints(list): list of integers containing one or more integers
   """
   if not ints:
      return None, None
   if len(ints) ==None:
      return None
   min_val = float("inf")
   max_val = -float("inf")
   # for each int in ints if update max_val and min_val accordingly
   for integer in ints:
      if integer > max_val:
         max_val = integer

      if integer < min_val:
         min_val = integer
         
   return (min_val, max_val)



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# edge cases
print("Pass" if ((5, 5) == get_min_max([2])) else "Fail") # equal numbers
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail") # negative and positive number
print("Pass" if ((None, None) == get_min_max([])) else "Fail") # empty list
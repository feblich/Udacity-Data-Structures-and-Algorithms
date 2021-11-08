def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # handle empty list
    if not input_list:
        return None
    # sort the list in descending order
    quicksort(input_list)
    input_list.reverse()
 
    # fill `x` with digits at the odd indices of the sorted list
    x = 0
    for i in range (0, len(input_list), 2):
        x = x * 10 + input_list[i]
 
    # fill `y` with digits at the even indices of the sorted list
    y = 0
    for i in range (1, len(input_list), 2):
        y = y * 10 + input_list[i]
 
    # print `x` and `y`
    print("The two numbers with maximum sum are", x, "and", y)
    return x, y

def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if not output and output == solution:
        print("List is empty")
        print("Pass")
        return
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# edge cases
test_case = [[1,1,1], [11, 1]]
test_function(test_case)

test_case = [[1], [1]]
test_function(test_case)

test_case = [[], None]
test_function(test_case)
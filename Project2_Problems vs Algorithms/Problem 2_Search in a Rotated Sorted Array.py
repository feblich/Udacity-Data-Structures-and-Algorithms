def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    low = 0
    high = len(input_list) - 1
    pivot_index = find_pivot(low, high, input_list)
    if number == input_list[pivot_index]:
        return pivot_index
    
    if number in input_list[pivot_index:]:
        return binary_search(input_list[pivot_index:], low, len(input_list[pivot_index:])-1, number)
    else:
        return binary_search(input_list[0:pivot_index], low, len(input_list[0:pivot_index])-1, number)

def find_pivot(start, end, input_list):
    mid = start + (end - start) // 2
    pivot_index = 0

    if input_list[mid] > input_list[mid + 1]:
        return mid + 1
    else:
        if input_list[start] > input_list[mid]:
            # It means that pivot is in left of mid
            pivot_index = find_pivot(start, mid-1, input_list)
        else:
            # It means that pivot is in the right of mid
            pivot_index = find_pivot(mid+1, end, input_list)

    return pivot_index

def binary_search(array, low, high, number):

    if high >= low:
        mid = (low + high) // 2

        if array[mid] == number:
            return mid
        
        if array[mid] < number:
            return binary_search(array, mid+1, high, number)
        else:
            return binary_search(array, low, mid-1, number)
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
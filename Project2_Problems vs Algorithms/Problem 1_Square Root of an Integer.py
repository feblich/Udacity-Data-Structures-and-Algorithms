
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    # handle 0 and 1 as special cases
    if (number == 0 or number == 1):
        return number

    start = 1
    end = number

    while start <= end:
        
        mid_value = (start + end) // 2

        if (mid_value*mid_value) == number:
            return mid_value

        if (mid_value*mid_value) < number:
            start = mid_value + 1  # get rid of half of the numbers
            result = mid_value

        else:
            end = mid_value - 1

    return result


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

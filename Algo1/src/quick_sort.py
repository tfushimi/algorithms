"""
Divide and Conquer, Sorting and Searching, and Randomized Algorithms
Programming assignment3
"""

def last_rule(array, start, end):
    """
    Used as a helper function of QuickSort()
    Choose the last element as a pivot
    The first element will be a pivot

    Args :
    array: array of numbers
    start: start index
    end: ending index

    Returns :
    None
    """
    array[start], array[end-1] = array[end-1], array[start]

def median_of_three_rule(array, start, end):
    """
    Used as a helper function of QuickSort()
    Choose the median of three as a pivot
    => pivot = median(array[start], array[end], array[middle])
    => e.g., [5, 3, 6, 2] => pivot = median(5, 3, 2) = 3 (in this case, array[middle] is 3 not 6!!!)
    => e.g., [5, 3, 6, 2, 1] => pivot = median(5, 6, 1) = 5 (in this case, array[middle] is 6)
    The first element will be a pivot

    Args :
    array: array of numbers
    start: start index
    end: ending index

    Returns:
    None
    """
    # get middle index
    n = end - start
    middle = n // 2 + start
    if n % 2 == 0:
        middle  -= 1
    # find middle
    pivot_index = start
    if array[start] < array[middle] < array[end-1] or array[end-1] < array[middle] < array[start]:
        pivot_index = middle
    elif array[start] < array[end-1] < array[middle] or array[middle] < array[end-1] < array[start]:
        pivot_index = end-1
    array[start], array[pivot_index] = array[pivot_index], array[start]

def partition(array, start, end):
    """
    Partition array[start],...,array[end] in place
    array[start] has to be the pivot
    array will be [<pivot, pivot, pivot<]

    Args :
    array: array of numbers
    start: start index
    end: ending index

    Returns :
    index of pivot
    """
    i = start + 1
    for j in range(start+1, end):
        if array[j] < array[start]:
            array[j], array[i] = array[i], array[j] # swap
            i += 1 # increment the delimiter
    pivot_index = i - 1
    array[start], array[pivot_index] = array[pivot_index], array[start] # place the pivot at right position
    return pivot_index

def quick_sort(array, start, end, pivot_rule=None):
    """
     Quick Sort array in range of [start, end)
     Choose pivot based on pivot_rule.

     Args :
     array: array of numbers
     start: start index
     end: ending index
     pivot_rule: rule of choosing pivots (default is to choose the first element as a pivot)

     Returns :
     the number of comparisons
     """
    n = end - start
    # base case
    if n <= 1:
        return 0
    # recursion
    if pivot_rule:
        # swap so that the pivot is the first element
        pivot_rule(array, start=start, end=end)
    # partition using the first element as a pivot
    pivot_index = partition(array, start=start, end=end)
    # recursive call on the first half
    num_comp = pivot_index - start
    num_comp += quick_sort(array, start=start, end=pivot_index, pivot_rule=pivot_rule)
    # recursive call on the second half
    num_comp += end - pivot_index - 1
    num_comp += quick_sort(array, start=pivot_index+1, end=end, pivot_rule=pivot_rule)
    return num_comp

if __name__ == '__main__':
    from copy import deepcopy

    # Open and read the text file
    with open("QuickSortArray.txt") as file:
        quick_sort_array = [int(line.strip()) for line in file]

    # Test
    # size of array
    n = len(quick_sort_array)

    # first rule
    first_array = deepcopy(quick_sort_array)
    print("First_element_rule")
    print("The number of comparison: ", quick_sort(first_array, start=0, end=n))

    # last rule
    last_array = deepcopy(quick_sort_array)
    print("Last_element_rule")
    print("The number of comparison: ", quick_sort(last_array, start=0, end=n, pivot_rule=last_rule))

    # median rule
    median_array = deepcopy(quick_sort_array)
    print("Median_of_three_rule")
    print("The number of comparison: ", quick_sort(median_array, start=0, end=n, pivot_rule=median_of_three_rule))

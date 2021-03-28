"""
Divide and Conquer, Sorting and Searching, and Randomized Algorithms
Programming assignment2
"""

def count_split_inv(left, right):
    """
    1. Count the number of split inversions
    2. Use Merge Sort

    Args:
    left, right = two sorted lists

    Returns:
    the number of split inversions
    """
    split_count = 0
    sorted_array = []
    left_size, right_size = len(left), len(right)
    i, j = 0, 0
    while i < left_size and j < right_size:
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            split_count += left_size - i
            sorted_array.append(right[j])
            j += 1
    if i < left_size:
        sorted_array += left[i:]
    if j < right_size:
        sorted_array += right[j:]
    return sorted_array, split_count

def merge_and_count_split_inv(array):
    """
    1. Count the number of inversions in a list
    2. Use recursion

    Args :
    array: an unsorted list

    Returns:
    sorted array, the number of inversions
    """
    if len(array) <= 1:
        return array, 0
    n = len(array) // 2
    left_array, x = merge_and_count_split_inv(array[:n]) # 1st half of the array
    right_array, y = merge_and_count_split_inv(array[n:]) # 2nd half of the array
    sorted_array, z = count_split_inv(left_array, right_array) # count the split inversions
    return sorted_array, x + y + z

if __name__ =='__main__':
    # Open and read the text file
    with open("IntegerArray.txt") as file:
        integer_array = [int(line.strip()) for line in file]

    # test
    _, num_inversions = merge_and_count_split_inv(integer_array)
    print(num_inversions)
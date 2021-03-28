from bisect import bisect_left, bisect_right

def two_sum(array):
    sum_value = set()
    for x in array:
        # find the indices
        left = bisect_left(array, -10000 - x)
        right = bisect_right(array, 10000 - x)

        for y in array[left:right]:
            if x != y: # distinct numbers
                sum_value.add(x + y)

    return len(sum_value)

if __name__ == '__main__':
    array = []
    with open("/Users/Takahiro/MyProjects/Algorithms/Algo2/data/two_sum.txt") as file:
        for line in file:
            array.append(int(line))

    print(two_sum(sorted(array)))
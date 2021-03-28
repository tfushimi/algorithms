from heapq import heappush, heappop

def median_maintenance(stream):
    left, left_size = [], 0 # less than or equal, max heap
    right, right_size = [], 0 # greater than, min heap
    medians = []
    """
    invariants
    - left_size should be right_size or right_size + 1
    """
    for x in stream:
        if left_size == right_size:
            if (not right) or (x <= right[0]):
                heappush(left, -x)
            else:
                heappush(left, -heappop(right))
                heappush(right, x)
            left_size += 1
        elif left_size == right_size + 1:
            if x > -left[0]:
                heappush(right, x)
            else:
                heappush(right, -heappop(left))
                heappush(left, -x)
            right_size += 1
        medians.append(-left[0])
    return medians

if __name__ == '__main__':
    stream = []
    with open("/Users/Takahiro/MyProjects/Algorithms/Algo2/data/median.txt") as file:
        for line in file:
           x = int(line.split('\n')[0])
           stream.append(x)

    medians = median_maintenance(stream)
    print(f"Answer is {sum(medians)}")
    print(f"Answer is {sum(medians) % 10000}")

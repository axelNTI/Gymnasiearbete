# import random
# import time


def quicksort(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list
    randomItem = unsorted_list[0]
    less, equal, greater = [], [], []
    [
        less.append(i)
        if i < randomItem
        else equal.append(i)
        if i == randomItem
        else greater.append(i)
        for i in unsorted_list
    ]
    return quicksort(less) + equal + quicksort(greater)


def mergesort(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list
    left = mergesort(unsorted_list[: len(unsorted_list) // 2])
    right = mergesort(unsorted_list[len(unsorted_list) // 2 :])
    result = []
    while len(left) and len(right):
        result.append((left if left[0] <= right[0] else right).pop(0))
    [result.append(i) for i in left + right]
    return result


# quick1 = []
# generate = []

# for i in range(1000):
#     start = time.perf_counter_ns()
#     to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
#     generate.append(time.perf_counter_ns() - start)
#     start = time.perf_counter_ns()
#     quicksort(to_be_sorted)
#     quick1.append(time.perf_counter_ns() - start)

# print(f"Quick1: {sum(quick1) / (1000000*len(quick1))}")
# print(f"Generate: {sum(generate) / (1000000*len(generate))}")

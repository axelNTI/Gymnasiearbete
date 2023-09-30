import random
import time


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
        # left_index = 0
        # right_index = 0
        # if left
        result.append((left if left[0] <= right[0] else right).pop(0))
    [result.append(i) for i in left + right]
    return result


# quicksort_list = []
# mergesort_list = []

# for i in range(1000):
#     print(i)
#     to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
#     print('Quicksort')
#     start = time.perf_counter_ns()
#     quicksort(to_be_sorted)
#     quicksort_list.append(time.perf_counter_ns() - start)
#     print('Mergesort')
#     start = time.perf_counter_ns()
#     mergesort(to_be_sorted)
#     mergesort_list.append(time.perf_counter_ns() - start)


# print(f"Quicksort: {sum(quicksort_list) / (1000000*len(quicksort_list))}")
# print(f"Mergesort: {sum(mergesort_list) / (1000000*len(mergesort_list))}")

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
    sorted_list = []
    left_index = 0
    right_index = 0
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    while len(left) > left_index:
        sorted_list.append(left[left_index])
        left_index += 1
    while len(right) > right_index:
        sorted_list.append(right[right_index])
        right_index += 1
    return sorted_list


quicksort_list = []
mergesort_list = []


for i in range(100):
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
    start = time.perf_counter_ns()
    quicksort(to_be_sorted)
    quicksort_list.append(time.perf_counter_ns() - start)
    start = time.perf_counter_ns()
    mergesort(to_be_sorted)
    mergesort_list.append(time.perf_counter_ns() - start)


print(f"Quicksort: {sum(quicksort_list) / (1000000*len(quicksort_list))}")
print(f"Mergesort: {sum(mergesort_list) / (1000000*len(mergesort_list))}")

import random
import time
from numpy import sign


def quicksort1(unsorted_list) -> list:
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
    return quicksort1(less) + equal + quicksort1(greater)


def quicksort2(unsorted_list) -> list:
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
    return quicksort2(less) + equal + quicksort2(greater)


def quicksort3(unsorted_list) -> list:
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
    return quicksort3(less) + equal + quicksort3(greater)


def quicksort4(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list
    randomItem = unsorted_list[0]
    less, equal, greater = [], [], []
    for i in unsorted_list:
        locals()[["equal", "greater", "less"][sign(i - randomItem)]].append(i)
    # [
    #     less.append(i)
    #     if i < randomItem
    #     else equal.append(i)
    #     if i == randomItem
    #     else greater.append(i)
    #     for i in unsorted_list
    # ]
    return quicksort4(less) + equal + quicksort4(greater)


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


quicksort1_list = []
quicksort2_list = []
quicksort3_list = []
quicksort4_list = []


for i in range(1000):
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
    start1 = time.perf_counter_ns()
    quicksort1(to_be_sorted)
    quicksort1_list.append(time.perf_counter_ns() - start1)
    start2 = time.perf_counter_ns()
    quicksort2(to_be_sorted)
    quicksort2_list.append(time.perf_counter_ns() - start2)
    start3 = time.perf_counter_ns()
    quicksort3(to_be_sorted)
    quicksort3_list.append(time.perf_counter_ns() - start3)
    start4 = time.perf_counter_ns()
    quicksort4(to_be_sorted)
    quicksort4_list.append(time.perf_counter_ns() - start4)


print(f"Quicksort1: {sum(quicksort1_list) / (1000000*len(quicksort1_list))}")
print(f"Quicksort2: {sum(quicksort2_list) / (1000000*len(quicksort2_list))}")
print(f"Quicksort3: {sum(quicksort3_list) / (1000000*len(quicksort3_list))}")
print(f"Quicksort4: {sum(quicksort4_list) / (1000000*len(quicksort4_list))}")

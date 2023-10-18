import random
import time


def quicksort(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = len(unsorted_list) // 2
    if unsorted_list[0] > unsorted_list[mid]:
        unsorted_list[0], unsorted_list[mid] = unsorted_list[mid], unsorted_list[0]
    if unsorted_list[0] > unsorted_list[-1]:
        unsorted_list[0], unsorted_list[-1] = unsorted_list[-1], unsorted_list[0]
    if unsorted_list[mid] > unsorted_list[-1]:
        unsorted_list[mid], unsorted_list[-1] = unsorted_list[-1], unsorted_list[mid]
    pivot = unsorted_list[mid]
    left, equal, right = [], [], []
    for i in unsorted_list:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            equal.append(i)
        elif i > pivot:
            right.append(i)
    return quicksort(left) + equal + quicksort(right)


def quicksort2(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list
    randomItem = unsorted_list[0]
    less, equal, greater = [], [], []
    [
        [equal, greater, less][numpy.sign(i - randomItem)].append(i)
        for i in unsorted_list
    ]
    return quicksort2(less) + equal + quicksort2(greater)


def mergesort(unsorted_list) -> list:
    if len(unsorted_list) < 2:
        return unsorted_list
    left = mergesort(unsorted_list[: len(unsorted_list) // 2])
    right = mergesort(unsorted_list[len(unsorted_list) // 2 :])
    sorted_list = []
    left_index = 0
    right_index = 0
    left_len = len(left)
    right_len = len(right)
    while left_len > left_index and right_len > right_index:
        left_item = left[left_index]
        right_item = right[right_index]
        if left_item <= right_item:
            sorted_list.append(left_item)
            left_index += 1
        else:
            sorted_list.append(right_item)
            right_index += 1
    while left_len > left_index:
        sorted_list.append(left[left_index])
        left_index += 1
    while right_len > right_index:
        sorted_list.append(right[right_index])
        right_index += 1
    return sorted_list


def introsort(unsorted_list) -> list:
    pass


def heapsort(unsorted_list) -> list:
    pass


def blocksort(unsorted_list) -> list:
    pass


def timsort(unsorted_list) -> list:
    pass


def cubesort(unsorted_list) -> list:
    pass


def treesort(unsorted_list) -> list:
    pass


def librarysort(unsorted_list) -> list:
    pass


def patiencesort(unsorted_list) -> list:
    pass


def smoothsort(unsorted_list) -> list:
    pass


def tournamentsort(unsorted_list) -> list:
    pass


quicksort_list = []
quicksort2_list = []
mergesort_list = []
introsort_list = []
heapsort_list = []
blocksort_list = []
timsort_list = []
cubesort_list = []
treesort_list = []
librarysort_list = []
patiencesort_list = []
smoothsort_list = []
tournesort_list = []


for i in range(1000):
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for _ in range(10000)]

    quick_start = time.perf_counter_ns()
    quicksort(to_be_sorted)
    quicksort_list.append(time.perf_counter_ns() - quick_start)

    # quick_start2 = time.perf_counter_ns()
    # quicksort2(to_be_sorted)
    # quicksort2_list.append(time.perf_counter_ns() - quick_start2)

    # merge_start = time.perf_counter_ns()
    # mergesort(to_be_sorted)
    # mergesort_list.append(time.perf_counter_ns() - merge_start)

    # intro_start = time.perf_counter_ns()
    # introsort(to_be_sorted)
    # introsort_list.append(time.perf_counter_ns() - intro_start)

    # heap_start = time.perf_counter_ns()
    # heapsort(to_be_sorted)
    # heapsort_list.append(time.perf_counter_ns() - heap_start)

    # block_start = time.perf_counter_ns()
    # blocksort(to_be_sorted)
    # blocksort_list.append(time.perf_counter_ns() - block_start)

    # tim_start = time.perf_counter_ns()
    # timsort(to_be_sorted)
    # timsort_list.append(time.perf_counter_ns() - tim_start)

    # cube_start = time.perf_counter_ns()
    # cubesort(to_be_sorted)
    # cubesort_list.append(time.perf_counter_ns() - cube_start)

    # tree_start = time.perf_counter_ns()
    # treesort(to_be_sorted)
    # treesort_list.append(time.perf_counter_ns() - tree_start)

    # library_start = time.perf_counter_ns()
    # librarysort(to_be_sorted)
    # librarysort_list.append(time.perf_counter_ns() - library_start)

    # patience_start = time.perf_counter_ns()
    # patiencesort(to_be_sorted)
    # patiencesort_list.append(time.perf_counter_ns() - patience_start)

    # smooth_start = time.perf_counter_ns()
    # smoothsort(to_be_sorted)
    # smoothsort_list.append(time.perf_counter_ns() - smooth_start)

    # tournament_start = time.perf_counter_ns()
    # tournamentsort(to_be_sorted)
    # tournesort_list.append(time.perf_counter_ns() - tournament_start)


print(f"Quicksort: {sum(quicksort_list) / (1000000*len(quicksort_list))}")
# print(f"Quicksort2: {sum(quicksort2_list) / (1000000*len(quicksort2_list))}")
# print(f"Mergesort: {sum(mergesort_list) / (1000000*len(mergesort_list))}")
# print(f"Introsort: {sum(introsort_list) / (1000000*len(introsort_list))}")
# print(f"Heapsort: {sum(heapsort_list) / (1000000*len(heapsort_list))}")
# print(f"Blocksort: {sum(blocksort_list) / (1000000*len(blocksort_list))}")
# print(f"Timsort: {sum(timsort_list) / (1000000*len(timsort_list))}")
# print(f"Cubesort: {sum(cubesort_list) / (1000000*len(cubesort_list))}")
# print(f"Treesort: {sum(treesort_list) / (1000000*len(treesort_list))}")
# print(f"Librarysort: {sum(librarysort_list) / (1000000*len(librarysort_list))}")
# print(f"Patiencesort: {sum(patiencesort_list) / (1000000*len(patiencesort_list))}")
# print(f"Smoothsort: {sum(smoothsort_list) / (1000000*len(smoothsort_list))}")
# print(f"Tournamentsort: {sum(tournesort_list) / (1000000*len(tournesort_list))}")

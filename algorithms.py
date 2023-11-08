import random
import time


def quicksort(arr) -> list:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    if arr[0] > arr[mid]:
        arr[0], arr[mid] = arr[mid], arr[0]
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    if arr[mid] > arr[-1]:
        arr[mid], arr[-1] = arr[-1], arr[mid]
    pivot = arr[mid]
    less, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return quicksort(less) + equal + quicksort(greater)


def mergesort(arr) -> list:
    if len(arr) < 2:
        return arr
    left = mergesort(arr[: len(arr) // 2])
    right = mergesort(arr[len(arr) // 2 :])
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


# def introsort(arr) -> list:
#     pass


def heapsort(arr):
    start = len(arr) // 2
    end = len(arr)
    while end > 1:
        if start > 0:
            start -= 1
        else:
            end -= 1
            arr[end], arr[0] = arr[0], arr[end]
        root = start
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    return arr


def blocksort(arr):
    blocks = []
    for i in range(0, len(arr), 3):
        block = arr[i : i + 3]
        blocks.append(sorted(block))
    result = []
    while blocks:
        min_idx = 0
        for i in range(1, len(blocks)):
            if blocks[i][0] < blocks[min_idx][0]:
                min_idx = i
        result.append(blocks[min_idx].pop(0))
        if len(blocks[min_idx]) == 0:
            blocks.pop(min_idx)
    return result


# def timsort(arr) -> list:
#     pass


# def cubesort(arr) -> list:
#     pass


# def treesort(arr) -> list:
#     pass


def librarysort(arr) -> list:
    pass


def patiencesort(arr) -> list:
    pass


def smoothsort(arr) -> list:
    pass


def tournamentsort(arr) -> list:
    pass


# to_be_sorted = [int(round(random.gauss(0, 100), 0)) for _ in range(15)]
# print(to_be_sorted)
# print(quicksort2(to_be_sorted))
# exit()
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

    quick_start2 = time.perf_counter_ns()
    quicksort2(to_be_sorted)
    quicksort2_list.append(time.perf_counter_ns() - quick_start2)

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
print(f"Quicksort2: {sum(quicksort2_list) / (1000000*len(quicksort2_list))}")
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

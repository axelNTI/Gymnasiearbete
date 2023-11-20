import math

# Helper functions:


# Algorithms to be compared:


def quicksort(arr: list) -> list:
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


def mergesort(arr: list) -> list:
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


def introsort(arr: list) -> list:
    def introsorting(arr: list, max_depth):
        if len(arr) < 16:
            right = len(arr) - 1
            for i in range(1, right + 1):
                key_item = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key_item:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key_item
            return arr
        elif max_depth == 0:
            return heapsort(arr)
        else:
            pivot = len(arr) // 2
            if arr[0] > arr[pivot]:
                arr[0], arr[pivot] = arr[pivot], arr[0]
            if arr[0] > arr[-1]:
                arr[0], arr[-1] = arr[-1], arr[0]
            if arr[pivot] > arr[-1]:
                arr[pivot], arr[-1] = arr[-1], arr[pivot]
            return introsorting(arr[1 : pivot - 1], max_depth - 1)

    max_depth = math.log2(len(arr)) * 2
    return introsorting(arr.copy(), max_depth)


def heapsort(arr: list) -> list:
    arr = arr.copy()
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


def timsort(arr: list) -> list:
    def merge(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        arr = []
        index_left = index_right = 0
        while len(arr) < len(left) + len(right):
            if left[index_left] <= right[index_right]:
                arr.append(left[index_left])
                index_left += 1
            else:
                arr.append(right[index_right])
                index_right += 1
            if index_right == len(right):
                arr += left[index_left:]
                break

            if index_left == len(left):
                arr += right[index_right:]
                break

        return arr

    def insertionsort(arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1
        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item
        return arr

    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertionsort(arr, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(
                left=arr[start : midpoint + 1], right=arr[midpoint + 1 : end + 1]
            )
            arr[start : start + len(merged_array)] = merged_array
        size *= 2

    return arr

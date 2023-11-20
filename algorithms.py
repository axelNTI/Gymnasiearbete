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

        if len(arr) < 16:
            return insertionsort(arr)
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
    return introsorting(arr, max_depth)


def heapsort(arr: list) -> list:
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


def blocksort(arr: list) -> list:
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


def patiencesort(arr: list) -> list:
    piles = []
    for i in arr:
        if not piles:
            temp = []
            temp.append(i)
            piles.append(temp)
        else:
            flag = True
            for j in piles:
                if i < j[-1]:
                    j.append(i)
                    flag = False
                    break
            if flag:
                temp = []
                temp.append(i)
                piles.append(temp)
    arr = []
    while True:
        minu = float("inf")
        index = -1
        for i, j in enumerate(piles):
            if minu > j[-1]:
                minu = j[-1]
                index = i
        arr.append(minu)
        piles[index].pop()
        if not piles[index]:
            piles.pop(index)
        if not piles:
            break
    return arr


def smoothsort(arr: list) -> list:
    n = len(arr)

    def leonardo(k):
        if k < 2:
            return 1
        return leonardo(k - 1) + leonardo(k - 2) + 1

    def heapify(start, end):
        i = start
        j = 0
        k = 0
        while k < end - start + 1:
            if k & 0xAAAAAAAA:
                j = j + i
                i = i >> 1
            else:
                i = i + j
                j = j >> 1

            k = k + 1
        while i > 0:
            j = j >> 1
            k = i + j
            while k < end:
                if arr[k] > arr[k - i]:
                    break
                arr[k], arr[k - i] = arr[k - i], arr[k]
                k = k + i
            i = j

    p = n - 1
    q = p
    r = 0
    while p > 0:
        if (r & 0x03) == 0:
            heapify(r, q)

        if leonardo(r) == p:
            r = r + 1
        else:
            r = r - 1
            q = q - leonardo(r)
            heapify(r, q)
            q = r - 1
            r = r + 1

        arr[0], arr[p] = arr[p], arr[0]
        p = p - 1
    for i in range(n - 1):
        j = i + 1
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return arr

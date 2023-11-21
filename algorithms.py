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
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        left = i
        right = min((i + min_run - 1), n - 1)
        if right is None:
            right = len(arr) - 1
        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            left = arr[start : midpoint + 1]
            right = arr[midpoint + 1 : end + 1]
            if len(left) == 0:
                merged_array = right
            elif len(right) == 0:
                merged_array = left
            else:
                arr2 = []
                index_left = index_right = 0
                while len(arr2) < len(left) + len(right):
                    if left[index_left] <= right[index_right]:
                        arr2.append(left[index_left])
                        index_left += 1
                    else:
                        arr2.append(right[index_right])
                        index_right += 1
                    if index_right == len(right):
                        arr2 += left[index_left:]
                        break

                    if index_left == len(left):
                        arr2 += right[index_right:]
                        break
                merged_array = arr2
            arr[start : start + len(merged_array)] = merged_array
        size *= 2

    return arr

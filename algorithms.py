import random
import time


def quicksort(unsorted_list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = random.choice(unsorted_list)
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


# def mergesort(unsorted_list):
#     if len(unsorted_list) <= 1:
#         return unsorted_list
#     left = []
#     right = []
#     for i in range(len(unsorted_list)):
#         if i < (len(unsorted_list)) / 2:
#             left.append(unsorted_list[i])
#         else:
#             right.append(unsorted_list[i])
#     result = []
#     while len(right) and len(right):
#         if left[0] <= right[0]:
#             result.append(left[0])
#             left.pop(0)
#         else:
#             result.append(right[0])
#             right.pop(0)
#     while len(left):
#         result.append(left[0])
#         left.pop(0)
#     while len(right):
#         result.append(right[0])
#         right.pop(0)
#     return result


def mergesort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left = mergesort(unsorted_list[: len(unsorted_list) // 2])
    right = mergesort(unsorted_list[len(unsorted_list) // 2 :])
    result = [i for i in unsorted_list]
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    [result.append(i) for i in left + right]
    return result


quick = []
merge = []
for i in range(100):
    print(i)
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
    start = time.time()
    quicksort(to_be_sorted)
    quick.append(time.time() - start)
    start = time.time()
    mergesort(to_be_sorted)
    merge.append(time.time() - start)

print(f"Quick: {1000*sum(quick) / len(quick)}")
print(f"Merge: {1000*sum(merge) / len(merge)}")

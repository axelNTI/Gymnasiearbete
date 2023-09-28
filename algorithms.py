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


def mergesort(unsorted_list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    left = mergesort(unsorted_list[: len(unsorted_list) // 2])
    right = mergesort(unsorted_list[len(unsorted_list) // 2 :])
    result = []
    while len(left) and len(right):
        result.append((left if left[0] <= right[0] else right).pop(0))
    [result.append(i) for i in left + right]
    return result


quick = []
merge = []
for i in range(10):
    print(i)
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(1000000)]
    start = time.time()
    print('Quick')
    quicksort(to_be_sorted)
    quick.append(time.time() - start)
    start = time.time()
    print('Merge')
    mergesort(to_be_sorted)
    merge.append(time.time() - start)

print(f"Quick: {1000*sum(quick) / len(quick)}")
print(f"Merge: {1000*sum(merge) / len(merge)}")

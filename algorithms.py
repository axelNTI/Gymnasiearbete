import random
import time


def quicksort(unsorted_list) -> list:
    short = True
    for i, j in enumerate(unsorted_list):
        if i == 2:
            short = False
            break
    if short:
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


def quicksort2(unsorted_list) -> list:
    short = True
    for i in enumerate(unsorted_list):
        if i[0] == 2:
            short = False
            break
    if short:
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
    return quicksort2(less) + equal + quicksort2(greater)


def quicksort3(unsorted_list) -> list:
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
    return quicksort3(less) + equal + quicksort3(greater)


def quicksort4(unsorted_list) -> list:
    try:
        unsorted_list[1]
    except:
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
    return quicksort4(less) + equal + quicksort4(greater)


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


quick1 = []
quick2 = []
quick3 = []
quick4 = []
python = []
for i in range(1000):
    print(i)
    to_be_sorted = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]
    start = time.perf_counter()
    quicksort(to_be_sorted)
    quick1.append(time.perf_counter()() - start)
    start = time.perf_counter()
    quicksort2(to_be_sorted)
    quick2.append(time.perf_counter()() - start)
    start = time.perf_counter()()
    quicksort3(to_be_sorted)
    quick3.append(time.perf_counter()() - start)
    start = time.perf_counter()()
    quicksort4(to_be_sorted)
    quick4.append(time.perf_counter()() - start)
    start = time.perf_counter()()
    to_be_sorted.sort()
    python.append(time.perf_counter()() - start)

print(f"Quick1: {sum(quick1) / len(quick1)}")
print(f"Quick2: {sum(quick2) / len(quick2)}")
print(f"Quick3: {sum(quick3) / len(quick3)}")
print(f"Quick4: {sum(quick4) / len(quick4)}")
print(f"Python: {sum(python) / len(python)}")

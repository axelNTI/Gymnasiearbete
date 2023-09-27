import random
import time

def quicksort(unsorted_list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = random.choice(unsorted_list)
    return (
        quicksort([i for i in unsorted_list if i < randomItem])
        + [i for i in unsorted_list if i == randomItem]
        + quicksort([i for i in unsorted_list if i < randomItem])
    )


def quicksort2(unsorted_list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = random.choice(unsorted_list)
    less = []
    equal = []
    greater = []
    for i in unsorted_list:
        if i < randomItem:
            less.append(i)
        elif i == randomItem:
            equal.append(i)
        else:
            greater.append(i)

    return quicksort2(less) + equal + quicksort2(greater)


def mergesort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left = []
    right = []
    for i in range(len(unsorted_list)):
        if i < (len(unsorted_list)) / 2:
            left.append(unsorted_list[i])
        else:
            right.append(unsorted_list[i])
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while len(right) and len(right):
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while len(left):
        result.append(left[0])
        left.pop(0)
    while len(right):
        result.append(right[0])
        right.pop(0)
    return result

quick1 = []
quick2 = []
for i in range(1000):
    unsorted = [random.randint(0, 1000) for i in range(10000)]
    start = time.time()
    quicksort(unsorted)
    quick1.append(time.time() - start)
    start = time.time()
    quicksort2(unsorted)
    quick2.append(time.time() - start)

print(f'1: {sum(quick1) / len(quick1)}')
print(f'2: {sum(quick2) / len(quick2)}')

# Kör tester på quicksort
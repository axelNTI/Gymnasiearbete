import time
import numpy as np


def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return quicksort(less) + equal + quicksort(greater)


def nquicksort(arr: np.ndarray) -> np.ndarray:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less, equal, greater = np.zeros(), np.zeros(), np.zeros()
    print(type(less))
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return nquicksort(less) + equal + nquicksort(greater)


quick = []
nquick = []

for i in range(100):
    array = np.random.normal(loc=0, scale=0.1, size=1000)
    quicklist = list(array.copy())
    time_start = time.perf_counter_ns()
    quicksort(quicklist)
    quick.append(time.perf_counter_ns() - time_start)
    nquicklist = array.copy()
    ntime_start = time.perf_counter_ns()
    nquicksort(nquicklist)
    nquick.append(time.perf_counter_ns() - ntime_start)

print(sum(quick) / len(quick))
print(sum(nquick) / len(nquick))

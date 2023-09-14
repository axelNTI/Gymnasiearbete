import random
import time
import itertools
import matplotlib
import numpy  # https://math.stackexchange.com/questions/1568900/generating-random-numbers-of-bell-curve-distribution
import threading  # Kolla hur man väljer att köra på performance-cores && Multiprocessing vs Multithreding


def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = random.choice(unsorted_list)
    return (
        quicksort([i for i in unsorted_list if i < randomItem])
        + [i for i in unsorted_list if i == randomItem]
        + quicksort([i for i in unsorted_list if i < randomItem])
    )


time_list = []

for i in range(10):
    random_list = [random.randint(0, 100000) for i in range(1000000)]
    start_time = time.time()
    quicksort(random_list)
    print(end_time := time.time() - start_time)
    time_list.append(end_time)

print(sum(time_list) / len(time_list))

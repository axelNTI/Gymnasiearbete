import matplotlib.pyplot as mplp
import itertools
import random
import numpy
import time
import os

random.seed(os.urandom(256))


def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = random.choice(unsorted_list)
    return (
        quicksort([i for i in unsorted_list if i < randomItem])
        + [i for i in unsorted_list if i == randomItem]
        + quicksort([i for i in unsorted_list if i < randomItem])
    )


def sorting():
    time_list = []
    num_of_cycles = 10
    size = 1000000
    for i in range(num_of_cycles):
        print(f"{i/num_of_cycles * 100}%")
        random_list = [random.gauss(size / 2, size / 10) for i in range(size)]
        start_time = time.time()
        quicksort(random_list)
        time_list.append(time.time() - start_time)
    print(sum(time_list) / len(time_list))

size = 1000000
bins = size / 100
random_list = [random.gauss(0, 10) for i in range(size)]
mplp.hist(random_list, bins=bins)
mplp.show()
# sorting()

import matplotlib
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
    for i in range(num_of_cycles):
        print(f"{i/num_of_cycles * 100}%")
        random_list = [random.randint(0, 100000) for i in range(1000000)]
        start_time = time.time()
        quicksort(random_list)
        time_list.append(time.time() - start_time)
    print(sum(time_list) / len(time_list))

sorting()
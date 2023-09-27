import matplotlib.pyplot as mplp
from numba import jit, cuda
import itertools
import random

# import timeit

import numpy
import time
import os
from algorithms import *

random.seed(os.urandom(256))





random_list = [int(round(random.gauss(0, 3), 0)) for i in range(10)]


def func():
    cpu_list = []
    for i in range(10):
        start = time.time()
        quicksort(random_list)
        cpu_list.append(time.time() - start)
    print(f"CPU: {sum(cpu_list) / len(cpu_list)}")


# function optimized to run on gpu
@jit(target_backend="cuda")
def func2():
    gpu_list = []
    for i in range(10):
        start = time.time()
        quicksort(random_list)
        gpu_list.append(time.time() - start)
    print(f"GPU: {sum(gpu_list) / len(gpu_list)}")


# print(timeit.timeit('quicksort(random_list)', number=100))
# print(timeit.timeit('quicksort(random_list)', number=100))


if __name__ == "__main__":
    func()
    func2()


# def sorting():
#     time_list = []
#     num_of_cycles = 10
#     size = 1000000
#     for i in range(num_of_cycles):
#         print(f"{i/num_of_cycles * 100}%")
#         random_list = [int(round(random.gauss(0, 3), 0)) for i in range(10)]
#         start_time = timeit.timeit()
#         quicksort(random_list)
#         time_list.append(time.time() - start_time)
#     print(sum(time_list) / len(time_list))

# random_list = [int(round(random.gauss(0, 3), 0)) for i in range(10)]
# print(random_list)


# size = 1000000
# bins = size / 100
# random_list = [random.gauss(0, 10) for i in range(size)]
# mplp.hist(random_list, bins=bins)
# mplp.show()
# sorting()

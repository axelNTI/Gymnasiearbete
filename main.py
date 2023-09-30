import matplotlib.pyplot as mplp
from numba import cuda
import itertools
import random
import numpy
import time
import os
from algorithms import *

random.seed(os.urandom(256))

print(cuda.gpus)

random_list = [int(round(random.gauss(0, 100), 0)) for i in range(10000)]


def func():
    cpu_list = []
    for i in range(1000):
        start = time.perf_counter_ns()
        quicksort(random_list)
        cpu_list.append(time.perf_counter_ns() - start)
    # print(f"CPU: {sum(cpu_list) / (1000000*len(cpu_list))}")


@cuda.jit
def func2():
    gpu_list = []
    for i in range(1000):
        start = time.perf_counter_ns()
        quicksort(random_list)
        gpu_list.append(time.perf_counter_ns() - start)
    # print(f"GPU: {sum(gpu_list) / (1000000*len(gpu_list))}")


​
# Create the data array - usually initialized some other way
data = numpy.ones(256)

# Set the number of threads in a block
threadsperblock = 32 

# Calculate the number of thread blocks in the grid
blockspergrid = (data.size + (threadsperblock - 1)) // threadsperblock

# Now start the kernel
func2[blockspergrid, threadsperblock](data)

# Print the result
print(data)



# if __name__ == "__main__":
#     func()
#     func2()


# def sorting():
#     time_list = []
#     num_of_cycles = 10
#     size = 1000000
#     for i in range(num_of_cycles):
#         print(f"{i/num_of_cycles * 100}%")
#         random_list = [int(round(random.gauss(0, 3), 0)) for i in range(10)]
#         start_time = timeit.timeit()
#         quicksort(random_list)
#         time_list.append(time.time_perf_counter_ns() - start_time)
#     print(sum(time_list) / len(time_list))

# random_list = [int(round(random.gauss(0, 3), 0)) for i in range(10)]
# print(random_list)


# size = 1000000
# bins = size / 100
# random_list = [random.gauss(0, 10) for i in range(size)]
# mplp.hist(random_list, bins=bins)
# mplp.show()
# sorting()

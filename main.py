import random
import time
import os
from algorithms import *

# results = {
#     "Quicksort": {"1000", "10000", "100000"},
#     "Mergesort": {},
#     "Introsort": {},
#     "Heapsort": {},
#     "Timsort": {},
# }


class Result:
    def __init__(self, time_ns, algorithm, size, deviation) -> None:
        self.time_ns = time_ns
        self.algorithm = algorithm
        self.size = size
        self.deviation = deviation


random.seed(os.urandom(255))
sizes = (1000, 10000, 100000)
deviations = (0.1, 0.01, 0.001)
iterations = 25000
results_list = []
for iteration in range(iterations):
    for size in sizes:
        for deviation in deviations:
            print(iteration, size, deviation)
            to_be_sorted = [
                int(round(random.gauss(0, deviation * size), 0)) for _ in range(size)
            ]

            quick_start = time.perf_counter_ns()
            quicksort(to_be_sorted.copy())
            quick_end = time.perf_counter_ns()
            results_list.append(
                Result(quick_end - quick_start, "Quicksort", size, deviation)
            )

            merge_start = time.perf_counter_ns()
            mergesort(to_be_sorted.copy())
            merge_end = time.perf_counter_ns()
            results_list.append(
                Result(merge_end - merge_start, "Mergesort", size, deviation)
            )

            intro_start = time.perf_counter_ns()
            introsort(to_be_sorted.copy())
            intro_end = time.perf_counter_ns()
            results_list.append(
                Result(intro_end - intro_start, "Introsort", size, deviation)
            )

            heap_start = time.perf_counter_ns()
            heapsort(to_be_sorted.copy())
            heap_end = time.perf_counter_ns()
            results_list.append(
                Result(heap_end - heap_start, "Heapsort", size, deviation)
            )

            tim_start = time.perf_counter_ns()
            timsort(to_be_sorted.copy())
            tim_end = time.perf_counter_ns()
            results_list.append(Result(tim_end - tim_start, "Timsort", size, deviation))


with open("data_storage.txt", "a") as file:
    file.write(str(results_list))

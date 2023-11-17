import random
import time
import os
from algorithms import *

random.seed(os.urandom(255))

iterations = 1000
size = 1000
deviation = size / 100
quicksort_list = []
mergesort_list = []
introsort_list = []
heapsort_list = []
blocksort_list = []
timsort_list = []
patiencesort_list = []
smoothsort_list = []
tournamentsort_list = []

for i in range(iterations):
    print(i)
    to_be_sorted = [int(round(random.gauss(0, deviation), 0)) for _ in range(size)]

    quick_start = time.perf_counter_ns()
    quicksort(to_be_sorted)
    quicksort_list.append(time.perf_counter_ns() - quick_start)

    merge_start = time.perf_counter_ns()
    mergesort(to_be_sorted)
    mergesort_list.append(time.perf_counter_ns() - merge_start)

    intro_start = time.perf_counter_ns()
    introsort(to_be_sorted)
    introsort_list.append(time.perf_counter_ns() - intro_start)

    heap_start = time.perf_counter_ns()
    heapsort(to_be_sorted)
    heapsort_list.append(time.perf_counter_ns() - heap_start)

    block_start = time.perf_counter_ns()
    blocksort(to_be_sorted)
    blocksort_list.append(time.perf_counter_ns() - block_start)

    tim_start = time.perf_counter_ns()
    timsort(to_be_sorted)
    timsort_list.append(time.perf_counter_ns() - tim_start)

    patience_start = time.perf_counter_ns()
    patiencesort(to_be_sorted)
    patiencesort_list.append(time.perf_counter_ns() - patience_start)

    smooth_start = time.perf_counter_ns()
    smoothsort(to_be_sorted)
    smoothsort_list.append(time.perf_counter_ns() - smooth_start)

    tournament_start = time.perf_counter_ns()
    tournamentsort(to_be_sorted)
    tournamentsort_list.append(time.perf_counter_ns() - tournament_start)

print(f"Quicksort: { sum(quicksort_list) / (1000000*iterations)} ms")
print(f"Mergesort: { sum(mergesort_list) / (1000000*iterations)} ms")
print(f"Introsort: { sum(introsort_list) / (1000000*iterations)} ms")

print(f"Heapsort: { sum(heapsort_list) / (1000000*iterations)} ms")
print(f"Blocksort: { sum(blocksort_list) / (1000000*iterations)} ms")
print(f"Timsort: { sum(timsort_list) / (1000000*iterations)} ms")

print(f"Patiencesort: { sum(patiencesort_list) / (1000000*iterations)} ms")
print(f"Smoothsort: { sum(smoothsort_list) / (1000000*iterations)} ms")
print(f"Tournamentsort: { sum(tournamentsort_list) / (1000000*iterations)} ms")

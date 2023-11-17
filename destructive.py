import random
import os
from algorithms import *

#Algorithm testing. Will not be used during the trial.

random.seed(os.urandom(255))
algorithms = (
    "quicksort(unsorted_list)",
    "mergesort(unsorted_list)",
    "introsort(unsorted_list)",
    "heapsort(unsorted_list)",
    "blocksort(unsorted_list)",
    "timsort(unsorted_list)",
    "patiencesort(unsorted_list)",
    "smoothsort(unsorted_list)",
    "tournamentsort(unsorted_list)",
)

size = 10
deviation = size / 100

for i in range(100):
    print(i)
    unsorted_list = [int(round(random.gauss(0, deviation), 0)) for _ in range(size)]
    if quicksort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Quicksort failed on iteration {i}]")
    if mergesort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Mergesort failed on iteration {i}]")
    if introsort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Introsort failed on iteration {i}]")
    if heapsort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Heapsort failed on iteration {i}]")
    if blocksort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Blocksort failed on iteration {i}]")
    if timsort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Timsort failed on iteration {i}]")
    if patiencesort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Patiencesort failed on iteration {i}]")
    if smoothsort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Smoothsort failed on iteration {i}]")
    if tournamentsort(unsorted_list) != sorted(unsorted_list):
        raise Exception(f"Tournamentsort failed on iteration {i}]")
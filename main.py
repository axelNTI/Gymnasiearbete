import random as rand
import time as t
import itertools as it
import matplotlib as mpl
import numpy as num  # https://math.stackexchange.com/questions/1568900/generating-random-numbers-of-bell-curve-distribution
import multiprocessing as mp
# https://pythonspeed.com/articles/faster-multiprocessing-pickle/#:~:text=The%20multiprocessing%20module%20is%20built,benefits%20of%20using%20worker%20processes.


def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    randomItem = rand.choice(unsorted_list)
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
        random_list = [rand.randint(0, 100000) for i in range(1000000)]
        start_time = t.time()
        quicksort(random_list)
        time_list.append(t.time() - start_time)
    return time_list

    


if __name__ == "__main__":
    time_list = []
    for num in range(mp.cpu_count()):
        time_list.append(mp.Process(target=sorting).start())
    print(f"Average: {sum(time_list) / len(time_list)}")
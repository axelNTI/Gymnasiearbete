import pickle

# import matplotlib


class Result:
    def __init__(self, time_ns, algorithm, size, deviation) -> None:
        self.time_ns = time_ns
        self.algorithm = algorithm
        self.size = size
        self.deviation = deviation


with open("data.pkl", "rb") as file:
    results_list = pickle.load(file)


def average(arr: list) -> float:
    return sum(arr) / len(arr)


import matplotlib.pyplot as plt


def plot_list_as_graph(data):
    # Initialize empty dictionaries to store counts
    count_dict = {}

    # Count frequency of each element in the list
    for item in data:
        count_dict[item] = count_dict.get(item, 0) + 1

    # Extract x and y values from the dictionaries
    x_values = list(count_dict.keys())
    y_values = list(count_dict.values())

    # Plot the graph
    plt.bar(x_values, y_values)

    # Labeling the axes
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Adding title to the plot
    plt.title("Frequency of Values in List")
    print(count_dict)

    # Show the plot
    plt.show()


algorithms = ("Quicksort", "Mergesort", "Heapsort", "Timsort")
sizes = (1000, 10000, 100000)
deviations = (0.1, 0.01, 0.001)
list_of_lists = {
    f"{i}_{j}": {
        k: average(
            [
                l.time_ns * 1e-6
                for l in results_list
                if l.size == i and l.deviation == j and l.algorithm == k
            ]
        )
        for k in algorithms
    }
    for i in sizes
    for j in deviations
}
list_of_lists2 = {
    f"{i}_{j}": {
        k: [
            round(l.time_ns * 1e-6, 2)
            for l in results_list
            if l.size == i and l.deviation == j and l.algorithm == k
        ]
        for k in algorithms
    }
    for i in sizes
    for j in deviations
}
categories = [f"{i}_{j}" for i in sizes for j in deviations]
for i in categories:
    list_of_lists[i] = dict(sorted(list_of_lists[i].items(), key=lambda x: x[1]))
    print(i)
    print(list_of_lists[i])
quicksort = []
mergesort = []
heapsort = []
timsort = []
for i in list_of_lists:
    quicksort.append(list_of_lists[i]["Quicksort"])
    mergesort.append(list_of_lists[i]["Mergesort"])
    heapsort.append(list_of_lists[i]["Heapsort"])
    timsort.append(list_of_lists[i]["Timsort"])
list_of_lists2["1000_0.1"]["Quicksort"].sort()
print(average(quicksort))
print(average(mergesort))
print(average(heapsort))
print(average(timsort))
# print(list_of_lists2["10000_0.1"]["Quicksort"])
plot_list_as_graph(list_of_lists2["1000_0.1"]["Quicksort"])

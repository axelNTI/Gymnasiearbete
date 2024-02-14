import pickle
import plotly.express as px


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


def plot_list_as_graph(data, name, size, deviation):
    count_dict = {}
    for item in data:
        count_dict[item] = count_dict.get(item, 0) + 1
    x_values = list(count_dict.keys())
    y_values = list(count_dict.values())
    fig = px.bar(
        x=x_values,
        y=y_values,
        labels={"x": "Time (ms)", "y": "Amount"},
        title=f"Amount of times in algorithm: {name}. Size: {size}. Standard deviation: {size*deviation}.",
    )
    fig.show()


algorithms = ("Quicksort", "Mergesort", "Heapsort", "Timsort")
sizes = (1000, 10000, 100000)
deviations = (0.1, 0.01, 0.001)
list_of_averages = {
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
list_of_values = {
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
    list_of_averages[i] = dict(sorted(list_of_averages[i].items(), key=lambda x: x[1]))
    print(i)
    print(list_of_averages[i])
quicksort_times = []
mergesort_times = []
heapsort_times = []
timsort_times = []
for i in list_of_averages:
    quicksort_times.append(list_of_averages[i]["Quicksort"])
    mergesort_times.append(list_of_averages[i]["Mergesort"])
    heapsort_times.append(list_of_averages[i]["Heapsort"])
    timsort_times.append(list_of_averages[i]["Timsort"])
print(average(quicksort_times))
print(average(mergesort_times))
print(average(heapsort_times))
print(average(timsort_times))
[
    plot_list_as_graph(
        list_of_values[f"{size}_{deviation}"][algorithm],
        algorithm,
        size,
        deviation,
    )
    for algorithm in algorithms
    for size in sizes
    for deviation in deviations
]

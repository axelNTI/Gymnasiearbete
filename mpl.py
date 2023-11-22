import pickle


class Result:
    def __init__(self, time_ns, algorithm, size, deviation) -> None:
        self.time_ns = time_ns
        self.algorithm = algorithm
        self.size = size
        self.deviation = deviation


with open("data.pkl", "rb") as file:
    results_list = pickle.load(file)

algorithms = ("Quicksort", "Mergesort", "Heapsort", "Timsort")
sizes = (1000, 10000, 100000)
deviations = (0.1, 0.01, 0.001)
# list_of_lists = []
#
# for i in algorithms:
#     for j in sizes:
#         for k in deviations:
#             locals()[f"{i}_{j}_{k}"] = [
#                 l
#                 for l in results_list
#                 if l.algorithm == i and l.size == j and l.deviation == k
#             ]
#             list_of_lists.append(locals()[f"{i}_{j}_{k}"])
list_of_lists = {
    f"{i}_{j}_{k}": [
        l for l in results_list if l.algorithm == i and l.size == j and l.deviation == k
    ]
    for i in algorithms
    for j in sizes
    for k in deviations
}
for i, j in [(i, j) for i in sizes for j in deviations]:
    print(f"{i}_{j}")

import pickle


class Result:
    def __init__(self, time_ns, algorithm, size, deviation) -> None:
        self.time_ns = time_ns
        self.algorithm = algorithm
        self.size = size
        self.deviation = deviation


with open("data.pkl", "rb") as file:
    results_list = pickle.load(file)

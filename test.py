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

    # Show the plot
    plt.show()


# Example usage
my_list = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7]
plot_list_as_graph(my_list)

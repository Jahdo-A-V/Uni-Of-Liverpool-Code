import itertools
import sys
import time

MAX_LENGTH = 5  # Assuming MAX_LENGTH is defined elsewhere

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm.
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])
    # Return the updated distance matrix
    return distance

def floyd_recursive(distance, k=0):
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Base case: If all intermediate nodes have been considered, return the distance matrix
    if k == MAX_LENGTH:
        return distance

    new_distance = [[0 for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]

    def update_distances(start_node, end_node):
        """
        Recursively updates the distances between all pairs of nodes.
        """
        # Base case for recursion
        if start_node == MAX_LENGTH:
            return
        elif end_node == MAX_LENGTH:
            update_distances(start_node + 1, 0)
        else:
            if start_node == end_node:
                new_distance[start_node][end_node] = 0
            else:
                new_distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][k] + distance[k][end_node]
                )
            update_distances(start_node, end_node + 1)

    # Start the recursive update process
    update_distances(0, 0)
    # Recursively process the next intermediate node
    return floyd_recursive(new_distance, k + 1)

def measure_execution_time(graph, algorithm):
    start_time = time.time()
    if algorithm == "iterative":
        shortest_paths = floyd(graph)
    elif algorithm == "recursive":
        shortest_paths = floyd_recursive(graph)
    end_time = time.time()
    return end_time - start_time

# Define different graphs
graphs = [
    [
        [0, 1, 3, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, 1, sys.maxsize, 4],
        [sys.maxsize, sys.maxsize, 0, 2, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ],
    [
        [0, sys.maxsize, sys.maxsize, sys.maxsize, 10],
        [1, 0, sys.maxsize, 2, sys.maxsize],
        [sys.maxsize, 3, 0, sys.maxsize, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 1, sys.maxsize, 0]
    ],
    [
        [0, 4, sys.maxsize, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, 2, sys.maxsize, sys.maxsize],
        [1, sys.maxsize, 0, 6, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, 3],
        [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ],
    # Add more graphs as needed
]

# Measure execution time for each graph and algorithm
execution_times = {"iterative": [], "recursive": []}
for graph in graphs:
    execution_times["iterative"].append(measure_execution_time(graph, "iterative"))
    execution_times["recursive"].append(measure_execution_time(graph, "recursive"))

# Tabulate the execution times
print("\nGraph Execution Times:")
print("Graph\t\tIterative Time (seconds)\t\tRecursive Time (seconds)")
print("--------------------------------------------------------------")

import itertools
import sys
import time

MAX_LENGTH = 5  # Assuming MAX_LENGTH is defined elsewhere

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm.
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])
    # Return the updated distance matrix
    return distance

def floyd_recursive(distance, k=0):
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Base case: If all intermediate nodes have been considered, return the distance matrix
    if k == MAX_LENGTH:
        return distance

    new_distance = [[0 for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]

    def update_distances(start_node, end_node):
        """
        Recursively updates the distances between all pairs of nodes.
        """
        # Base case for recursion
        if start_node == MAX_LENGTH:
            return
        elif end_node == MAX_LENGTH:
            update_distances(start_node + 1, 0)
        else:
            if start_node == end_node:
                new_distance[start_node][end_node] = 0
            else:
                new_distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][k] + distance[k][end_node]
                )
            update_distances(start_node, end_node + 1)

    # Start the recursive update process
    update_distances(0, 0)
    # Recursively process the next intermediate node
    return floyd_recursive(new_distance, k + 1)

def measure_execution_time(graph, algorithm):
    start_time = time.time()
    if algorithm == "iterative":
        shortest_paths = floyd(graph)
    elif algorithm == "recursive":
        shortest_paths = floyd_recursive(graph)
    end_time = time.time()
    return end_time - start_time

# Define different graphs
graphs = [
    [
        [0, 1, 3, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, 1, sys.maxsize, 4],
        [sys.maxsize, sys.maxsize, 0, 2, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ],
    [
        [0, sys.maxsize, sys.maxsize, sys.maxsize, 10],
        [1, 0, sys.maxsize, 2, sys.maxsize],
        [sys.maxsize, 3, 0, sys.maxsize, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 1, sys.maxsize, 0]
    ],
    [
        [0, 4, sys.maxsize, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, 2, sys.maxsize, sys.maxsize],
        [1, sys.maxsize, 0, 6, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, 3],
        [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ],
    # Add more graphs as needed
]

# Measure execution time for each graph and algorithm
execution_times = {"iterative": [], "recursive": []}
for graph in graphs:
    execution_times["iterative"].append(measure_execution_time(graph, "iterative"))
    execution_times["recursive"].append(measure_execution_time(graph, "recursive"))

# Tabulate the execution times
for idx, (iter_time, recur_time) in enumerate(zip(execution_times["iterative"], execution_times["recursive"])):
    print(f"{idx + 1}\t\t{iter_time}\t\t{recur_time}")

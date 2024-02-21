import itertools
import sys
import time


# Iteration of Floyd warshall Algorithm 

MAX_LENGTH = 5  # Assuming MAX_LENGTH is defined elsewhere

def floyd(distance):
    """
    A iteration implementation of Floyd's algorithm
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

def measure_execution_time(graph):
    start_time = time.time()
    shortest_paths = floyd(graph)
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
    [
        [0, sys.maxsize, 8, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, 1, sys.maxsize, sys.maxsize],
        [4, sys.maxsize, 0, sys.maxsize, 2],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, 7],
        [sys.maxsize, 5, sys.maxsize, 1, 0]
    ],
    [
        [0, 2, 9, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, sys.maxsize, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, sys.maxsize, 4],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize],
        [7, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ],
]

# Measure execution time for each graph
execution_times = []
for idx, graph in enumerate(graphs):
    execution_time = measure_execution_time(graph)
    execution_times.append(execution_time)
    print(f"Graph {idx + 1}: Execution Time = {execution_time}")

# Tabulate the execution times
print("\nGraph Execution Times:")
print("Graph\t\tExecution Time (seconds)")
print("-----------------------------------")
for idx, time in enumerate(execution_times):
    print(f"{idx + 1}\t\t{time}")
    
    
# Recursion of Floyd warshall Algorithm 

MAX_LENGTH = 5  # Assuming MAX_LENGTH is defined elsewhere

def floyd_recursive(distance, k=0):
    """
    A recursive implementation of Floyd's algorithm.
    """
    # Base case: If all intermediate nodes have been considered, return the distance matrix
    if k == MAX_LENGTH:
        return distance

    # Create a new distance matrix for this iteration
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

def measure_execution_time(graph):
    start_time = time.time()
    shortest_paths = floyd_recursive(graph)
    end_time = time.time()
    return end_time - start_time, shortest_paths

# Example graphs
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
        [
            [0, sys.maxsize, 8, sys.maxsize, sys.maxsize],
            [sys.maxsize, 0, 1, sys.maxsize, sys.maxsize],
            [4, sys.maxsize, 0, sys.maxsize, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0, 7],
            [sys.maxsize, 5, sys.maxsize, 1, 0]
        ],
        [
            [0, 2, 9, sys.maxsize, sys.maxsize],
            [sys.maxsize, 0, sys.maxsize, 3, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, sys.maxsize, 4],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0, sys.maxsize],
            [7, sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ],
    ]

# Measure execution time for each graph
execution_times = []
for idx, graph in enumerate(graphs):
    execution_time = measure_execution_time(graph)
    execution_times.append(execution_time)
    print(f"Graph {idx + 1}: Execution Time = {execution_time}\n")

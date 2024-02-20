import itertools
import sys
import time

MAX_LENGTH = 5  # Assuming MAX_LENGTH is defined elsewhere

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node], distance[start_node][intermediate] + distance[intermediate][end_node])

    # Any value that has sys.maxsize has no path
    # print(distance)

# Assuming `graph` is defined elsewhere
graph = [
    [0, 1, 3, sys.maxsize, sys.maxsize],
    [sys.maxsize, 0, 1, sys.maxsize, 4],
    [sys.maxsize, sys.maxsize, 0, 2, sys.maxsize],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

start_time = time.time()
floyd(graph)
end_time = time.time()
iterative_execution_time = end_time - start_time
print("Iterative Implementation Execution Time:", iterative_execution_time)

# Number of vertices in the graph
V = 4

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

def floydWarshall(graph):
    """ Solves all pair shortest path
    via Floyd Warshall Algorithm using recursion """

    # dist[][] will be the output
    # matrix that will finally
    # have the shortest distances
    # between every pair of vertices
    dist = [[0] * V for _ in range(V)]

    # Initialize dist with the values
    # from the input graph
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    # Recursive function to calculate
    # shortest distances
    def recursive_floyd(k, i, j):
        # Base case: if k exceeds the number of vertices, return
        if k >= V:
            return
        # If vertex k is on the shortest path from i to j,
        # update the value of dist[i][j]
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        # Recursive calls to explore all possible intermediate vertices
        recursive_floyd(k, i, j)
        recursive_floyd(k+1, i, j)
        recursive_floyd(k, i, k)
        recursive_floyd(k, k, j)

    # Call the recursive function with initial parameters
    recursive_floyd(0, 0, 0)

    return dist

# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

# Driver's code
if __name__ == "__main__":
    """
               10
        (0)------->(3)
         |         /|\
       5 |          |
         |          | 1
        \|/         |
        (1)------->(2)
               3     """
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
            ]
    start_time = time.time()
    # Function call
    dist = floydWarshall(graph)
    end_time = time.time()
    recursive_execution_time = end_time - start_time
    print("Recursive Implementation Execution Time:", recursive_execution_time)

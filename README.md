# Floyd's Algorithm Implementation

This repository contains Python implementations of Floyd's algorithm for finding the shortest paths in a directed graph. The implementations include both iterative and recursive approaches.

## Contents

1. [Description](#description)
2. [Iterative Implementation](#iterative-implementation)
3. [Recursive Implementation](#recursive-implementation)
4. [Usage](#usage)
5. [Example Graphs](#example-graphs)
6. [Execution Times](#execution-times)
7. [License](#license)

## Description

Floyd's algorithm, also known as Floyd-Warshall algorithm, is used to find the shortest paths between all pairs of vertices in a weighted graph. It works for both positive and negative edge weights (but with no negative cycles).

## Iterative Implementation

The `floyd_iterative.py` file contains the iterative implementation of Floyd's algorithm. It uses nested loops to iteratively update the distance matrix until all shortest paths are found.

## Recursive Implementation

The `floyd_recursive.py` file contains the recursive implementation of Floyd's algorithm. It recursively explores all possible intermediate nodes to find the shortest paths between all pairs of vertices.

## Usage

To use the implementations, simply run the Python scripts `floyd_iterative.py` and `floyd_recursive.py`. Each script contains example graphs and measures the execution time of the algorithm for each graph.

## Example Graphs

The example graphs used in the implementations are defined in the scripts. Each graph is represented as an adjacency matrix with arbitrary edge weights.

## Execution Times

The execution times of both implementations for the example graphs are printed when the scripts are run. These execution times provide insights into the performance of the algorithms for different graph sizes and edge weights.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

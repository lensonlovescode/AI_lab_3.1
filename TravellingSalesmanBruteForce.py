#!/usr/bin/env python3
"""
Solves the travelling salesman problem using brute force which works
for a small graph
"""
from itertools import permutations

graph = [
   [0, 10, 15, 20],
   [10, 0, 35, 25],
   [15, 35, 0, 30],
   [20, 25, 30, 0]
]


def tsp_all_paths(graph):
    """
    TSP function implementations
    """
    n = len(graph)
    vertices = list(range(1, n))
    min_path_cost = float('inf')
    best_path = []

    print("All possible paths with their costs:\n")

    for perm in permutations(vertices):
        current_cost = 0
        k = 0
        path = [0] + list(perm) + [0]
        for i in range(len(perm)):
            current_cost += graph[k][perm[i]]
            k = perm[i]
        current_cost += graph[k][0]

        print(f"Path: {path} -> Cost: {current_cost}")

        if current_cost < min_path_cost:
            min_path_cost = current_cost
            best_path = path

    print("\nShortest Path:", best_path)
    print("Minimum Cost:", min_path_cost)
tsp_all_paths(graph)

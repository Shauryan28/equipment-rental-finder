# Equipment Rental Availability Finder

This project implements a solution for finding the shortest path to available equipment in a network of rental providers using Breadth-First Search (BFS).

## Problem Description

Equip9 manages a network of equipment rental providers. Each provider has connections with other providers, allowing customers to rent equipment even if their preferred provider does not have availability. Given a list of providers and their connections, this solution determines the shortest path to find the nearest available equipment of a given type.

## Features

- Finds the shortest path to available equipment using BFS
- Handles disconnected graphs
- Returns -1 if no path exists
- Type-hinted for better code clarity

## Usage

```python
from equipment_rental import find_equipment_path

# Example usage
n = 5  # number of providers
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]  # connections between providers
availability = {
    1: ["excavator"],
    2: [],
    3: ["bulldozer"],
    4: ["excavator"],
    5: ["crane"]
}
start_provider = 2
target_equipment = "excavator"

result = find_equipment_path(n, edges, availability, start_provider, target_equipment)
print(result)  # Output: [2, 3, 4]
```

## Time Complexity

- Building the graph: O(E) where E is the number of edges
- BFS traversal: O(V + E) where V is the number of vertices and E is the number of edges

## Space Complexity

O(V) for the visited set and queue 
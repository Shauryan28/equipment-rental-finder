# Equip9 Solutions

This repository contains solutions for three different problems related to equipment rental and maintenance management.

## 1. Equipment Rental Availability (Graph Algorithm – BFS/DFS)

Finds the shortest path to available equipment in a network of rental providers using BFS.

# Equipment Rental Availability

This solution implements a system for finding the shortest path to available equipment in a network of rental providers using Breadth-First Search (BFS).

## Problem Description

Equip9 manages a network of equipment rental providers. Each provider has connections with other providers, allowing customers to rent equipment even if their preferred provider does not have availability. Given a list of providers and their connections, this solution determines the shortest path to find the nearest available equipment of a given type.

## Features

- Finds the shortest path to available equipment using BFS
- Handles disconnected graphs
- Returns -1 if no path exists
- Type-hinted for better code clarity

## Implementation Details

The solution uses:
- BFS (Breadth-First Search) for finding shortest paths
- Adjacency list representation for the graph
- Type hints for better code maintainability

### Time Complexity
- Building the graph: O(E) where E is the number of edges
- BFS traversal: O(V + E) where V is the number of vertices and E is the number of edges

### Space Complexity
O(V) for the visited set and queue

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

## Test Cases

The solution includes test cases for:
1. Basic path finding
2. Disconnected graphs
3. Multiple available equipment
4. No available equipment

## Function Structure

- `find_equipment_path(n: int, edges: List[Tuple[int, int]], availability: Dict[int, List[str]], start_provider: int, target_equipment: str) -> List[int]`: Main function to find the shortest path to available equipment

[View Solution](README_RENTAL.md)

## 2. Optimal Equipment Deal Matching (Heap/Priority Queue)

Matches equipment buyers with sellers using a Priority Queue to find the best-priced deals.

[View Solution](README_DEAL_MATCHER.md)

## 3. Maintenance Log Analysis (Segment Tree)

Analyzes equipment maintenance logs using a Segment Tree for efficient range queries.

[View Solution](README_MAINTENANCE.md)

## Project Structure

```
equipment-rental-finder/
├── equipment_rental.py      # Solution for Equipment Rental Availability
├── equipment_deal_matcher.py # Solution for Optimal Equipment Deal Matching
├── maintenance_log_analyzer.py # Solution for Maintenance Log Analysis
├── README.md               # Main README file
├── README_RENTAL.md        # Documentation for Equipment Rental solution
├── README_DEAL_MATCHER.md  # Documentation for Deal Matching solution
└── README_MAINTENANCE.md   # Documentation for Maintenance Log solution
```

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/Shauryan28/equipment-rental-finder.git
```

2. Navigate to the project directory:
```bash
cd equipment-rental-finder
```

3. Run any of the solutions:
```bash
python equipment_rental.py
python equipment_deal_matcher.py
python maintenance_log_analyzer.py
```

## Features

Each solution includes:
- Efficient data structures for optimal performance
- Type hints for better code clarity
- Comprehensive documentation
- Test cases and examples
- Detailed complexity analysis

## License

This project is open source and available under the MIT License. 
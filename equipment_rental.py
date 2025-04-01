from collections import deque
from typing import List, Dict, Set, Tuple

def find_equipment_path(
    n: int,
    edges: List[Tuple[int, int]],
    availability: Dict[int, List[str]],
    start_provider: int,
    target_equipment: str
) -> List[int]:
    """
    Find the shortest path to a provider that has the requested equipment using BFS.
    
    Args:
        n: Number of rental providers
        edges: List of connections between providers
        availability: Dictionary mapping providers to their available equipment
        start_provider: The provider where the customer is searching
        target_equipment: The equipment type the customer needs
        
    Returns:
        List[int]: The shortest path to a provider with the equipment, or -1 if not found
    """
    # Build adjacency list representation of the graph
    graph: Dict[int, Set[int]] = {i: set() for i in range(1, n + 1)}
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    
    # Initialize BFS
    queue = deque([(start_provider, [start_provider])])
    visited = {start_provider}
    
    while queue:
        current_provider, path = queue.popleft()
        
        # Check if current provider has the equipment
        if target_equipment in availability.get(current_provider, []):
            return path
            
        # Explore neighbors
        for neighbor in graph[current_provider]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return -1

def main():
    # Example usage
    n = 5
    edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
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
    print(f"Shortest path to find {target_equipment}: {result}")

if __name__ == "__main__":
    main() 
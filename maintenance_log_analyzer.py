from typing import List, Tuple
from datetime import datetime
import math

class SegmentTree:
    def __init__(self, size: int):
        # Calculate the size of the segment tree array
        self.size = 2 ** math.ceil(math.log2(size))
        self.tree = [0] * (2 * self.size)
    
    def update(self, index: int, value: int) -> None:
        """
        Update the value at the given index in the segment tree.
        """
        # Convert to 0-based index for the tree
        pos = self.size + index
        
        # Update the leaf node
        self.tree[pos] = value
        
        # Update parent nodes
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def query(self, left: int, right: int) -> int:
        """
        Query the sum in the range [left, right].
        """
        # Convert to 0-based indices
        left += self.size
        right += self.size
        
        result = 0
        
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
            if right % 2 == 0:
                result += self.tree[right]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        
        return result

class MaintenanceLogAnalyzer:
    def __init__(self):
        self.date_to_index = {}  # Maps dates to indices in the segment tree
        self.index_to_date = []  # Maps indices back to dates
        self.segment_tree = None
    
    def _process_dates(self, maintenance_logs: List[Tuple[int, str, int]]) -> None:
        """
        Process dates and create mappings for the segment tree.
        """
        # Extract unique dates and sort them
        dates = sorted(set(log[1] for log in maintenance_logs))
        
        # Create mappings
        self.date_to_index = {date: idx for idx, date in enumerate(dates)}
        self.index_to_date = dates
        
        # Initialize segment tree
        self.segment_tree = SegmentTree(len(dates))
    
    def _date_to_index(self, date: str) -> int:
        """
        Convert a date string to its corresponding index in the segment tree.
        """
        return self.date_to_index[date]
    
    def add_maintenance_logs(self, maintenance_logs: List[Tuple[int, str, int]]) -> None:
        """
        Add maintenance logs to the analyzer.
        """
        # Process dates and initialize segment tree
        self._process_dates(maintenance_logs)
        
        # Add each maintenance log to the segment tree
        for _, date, cost in maintenance_logs:
            idx = self._date_to_index(date)
            self.segment_tree.update(idx, cost)
    
    def query_range(self, start_date: str, end_date: str) -> int:
        """
        Query the total maintenance cost in the given date range.
        """
        start_idx = self._date_to_index(start_date)
        end_idx = self._date_to_index(end_date)
        return self.segment_tree.query(start_idx, end_idx)

def analyze_maintenance_logs(
    maintenance_logs: List[Tuple[int, str, int]],
    queries: List[Tuple[str, str]]
) -> List[int]:
    """
    Analyze maintenance logs and answer queries about total costs in date ranges.
    
    Args:
        maintenance_logs: List of (equipment_id, date, cost) tuples
        queries: List of (start_date, end_date) tuples
        
    Returns:
        List of total maintenance costs for each query
    """
    analyzer = MaintenanceLogAnalyzer()
    analyzer.add_maintenance_logs(maintenance_logs)
    
    results = []
    for start_date, end_date in queries:
        total_cost = analyzer.query_range(start_date, end_date)
        results.append(total_cost)
    
    return results

def main():
    # Example usage
    maintenance_logs = [
        (101, "2024-01-01", 500),
        (102, "2024-01-10", 300),
        (101, "2024-01-15", 700)
    ]
    queries = [
        ("2024-01-01", "2024-01-10"),
        ("2024-01-01", "2024-01-15")
    ]
    
    results = analyze_maintenance_logs(maintenance_logs, queries)
    print("Query results:", results)  # Expected: [800, 1500]
    
    # Additional test cases
    test_logs = [
        (101, "2024-01-01", 500),
        (102, "2024-01-05", 300),
        (103, "2024-01-10", 200),
        (101, "2024-01-15", 700),
        (102, "2024-01-20", 400)
    ]
    test_queries = [
        ("2024-01-05", "2024-01-10"),  # Only one record
        ("2024-01-01", "2024-01-15"),  # Multiple records
        ("2024-01-20", "2024-01-20")   # Single day
    ]
    
    test_results = analyze_maintenance_logs(test_logs, test_queries)
    print("\nAdditional test results:", test_results)  # Expected: [500, 1700, 400]

if __name__ == "__main__":
    main() 
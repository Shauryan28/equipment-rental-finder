# Maintenance Log Analysis

This project implements an efficient system for analyzing equipment maintenance logs using a Segment Tree data structure. The system can quickly answer queries about total maintenance costs within specific date ranges.

## Problem Description

Equip9 tracks equipment maintenance history. Each piece of equipment has a maintenance log with records of maintenance costs over time. Given multiple queries asking for the total maintenance cost in a specific date range, this solution provides an efficient way to process these queries.

## Features

- Efficient range queries using Segment Tree data structure
- Handles multiple maintenance records per date
- Supports arbitrary date range queries
- Type-hinted for better code clarity
- Includes comprehensive test cases

## Implementation Details

The solution uses:
- Segment Tree for efficient range queries
- Date-to-index mapping for handling date ranges
- Type hints for better code maintainability

### Time Complexity
- Building the segment tree: O(n log n) where n is the number of unique dates
- Range queries: O(log n) where n is the number of unique dates
- Updates: O(log n) where n is the number of unique dates

### Space Complexity
O(n) where n is the number of unique dates

## Usage

```python
from maintenance_log_analyzer import analyze_maintenance_logs

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
print(results)  # Output: [800, 1500]
```

## Test Cases

The solution includes test cases for:
1. Basic range queries
2. Single-day queries
3. Multiple records in the same date range
4. Overlapping date ranges

## Class Structure

### SegmentTree
- `update(index: int, value: int)`: Updates a value in the tree
- `query(left: int, right: int)`: Queries the sum in a range

### MaintenanceLogAnalyzer
- `add_maintenance_logs(logs: List[Tuple[int, str, int]])`: Adds maintenance logs
- `query_range(start_date: str, end_date: str)`: Queries total cost in a date range

### Helper Functions
- `analyze_maintenance_logs(logs: List[Tuple[int, str, int]], queries: List[Tuple[str, str]])`: Main function to process logs and answer queries 
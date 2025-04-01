# Optimal Equipment Deal Matching

This project implements an efficient system for matching equipment buyers with sellers using a Priority Queue (Heap) data structure. The system finds the lowest-priced seller for each buyer's request while respecting the buyer's maximum price constraint.

## Problem Description

Equip9 allows buyers to place requests for specific equipment, and sellers list their available stock with a price. The goal is to match a buyer's request with the best-priced seller offering the requested equipment. The system efficiently finds the seller with the lowest price for each incoming request.

## Features

- Efficient matching using Priority Queue (Heap) data structure
- Handles multiple sellers for the same equipment type
- Respects buyer's maximum price constraints
- Returns None for requests that can't be matched
- Type-hinted for better code clarity

## Implementation Details

The solution uses:
- `heapq` for implementing the Priority Queue
- `defaultdict` for efficient storage of equipment prices
- Type hints for better code maintainability

### Time Complexity
- Adding a seller: O(log n) where n is the number of sellers for that equipment type
- Finding best match: O(1) for checking the lowest price
- Overall matching process: O(m log n) where m is the number of sellers and n is the maximum number of sellers for any equipment type

### Space Complexity
O(m) where m is the total number of sellers

## Usage

```python
from equipment_deal_matcher import match_requests

# Example usage
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

results = match_requests(requests, sellers)
print(results)  # Output: [45000, 68000]
```

## Test Cases

The solution includes test cases for:
1. Basic matching scenario
2. Multiple sellers for the same equipment
3. Requests with prices below available options
4. Non-existent equipment types

## Class Structure

### EquipmentDealMatcher
- `add_seller(equipment_type: str, price: int)`: Adds a seller's equipment and price
- `find_best_match(equipment_type: str, max_price: int)`: Finds the lowest price within budget

### Helper Functions
- `match_requests(requests: List[Tuple[str, int]], sellers: List[Tuple[str, int]])`: Main function to match requests with sellers 
from typing import List, Tuple, Optional
from collections import defaultdict
import heapq

class EquipmentDealMatcher:
    def __init__(self):
        # Dictionary to store equipment types and their prices using min-heaps
        self.equipment_prices: dict[str, List[Tuple[int, int]]] = defaultdict(list)
    
    def add_seller(self, equipment_type: str, price: int) -> None:
        """
        Add a seller's equipment and price to the system.
        Uses a min-heap to maintain lowest prices at the top.
        """
        # Push negative price to create a min-heap (heapq is a min-heap by default)
        heapq.heappush(self.equipment_prices[equipment_type], (price, id(price)))
    
    def find_best_match(self, equipment_type: str, max_price: int) -> Optional[int]:
        """
        Find the lowest price for a given equipment type that's within the max_price.
        Returns None if no matching seller is found.
        """
        if equipment_type not in self.equipment_prices:
            return None
            
        # Get the heap for this equipment type
        price_heap = self.equipment_prices[equipment_type]
        
        # If heap is empty, no sellers available
        if not price_heap:
            return None
            
        # Get the lowest price (first element of the heap)
        lowest_price = price_heap[0][0]
        
        # If lowest price is within budget, return it
        if lowest_price <= max_price:
            return lowest_price
            
        return None

def match_requests(
    requests: List[Tuple[str, int]],
    sellers: List[Tuple[str, int]]
) -> List[Optional[int]]:
    """
    Match buyer requests with the best-priced sellers.
    
    Args:
        requests: List of (equipment_type, max_price) tuples
        sellers: List of (equipment_type, price) tuples
        
    Returns:
        List of matched prices (or None if no match found)
    """
    matcher = EquipmentDealMatcher()
    
    # Add all sellers to the matcher
    for equipment_type, price in sellers:
        matcher.add_seller(equipment_type, price)
    
    # Match each request
    results = []
    for equipment_type, max_price in requests:
        best_price = matcher.find_best_match(equipment_type, max_price)
        results.append(best_price)
    
    return results

def main():
    # Example usage
    requests = [("excavator", 50000), ("bulldozer", 70000)]
    sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]
    
    results = match_requests(requests, sellers)
    print("Matched prices:", results)  # Expected: [45000, 68000]
    
    # Additional test cases
    test_requests = [
        ("crane", 100000),
        ("excavator", 40000),  # Below available prices
        ("bulldozer", 70000)
    ]
    test_sellers = [
        ("crane", 95000),
        ("excavator", 45000),
        ("excavator", 48000),
        ("bulldozer", 68000)
    ]
    
    test_results = match_requests(test_requests, test_sellers)
    print("\nAdditional test results:", test_results)  # Expected: [95000, None, 68000]

if __name__ == "__main__":
    main() 
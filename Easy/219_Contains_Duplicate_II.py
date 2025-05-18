"""
Problem #219: Contains Duplicate II

Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array 
such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Example:
Input: nums = [1,2,3,1], k = 3
Output: True
Explanation: nums[0] = nums[3] = 1, |0 - 3| = 3 <= k

Approach:
- Use a hash map to store each number and its most recent index.
- For each number, check if it has been seen before and if the distance between the current index and the previous index is ≤ k.
- If we find such a pair, return True.
- Otherwise, update the hash map with the current number and its index.
- If we finish iterating without finding duplicates within distance k, return False.

Time Complexity: O(n) — one pass through the array where n is the length of nums
  - Each lookup and insertion in the hash map takes O(1) on average
Space Complexity: O(n) — in the worst case, all elements are unique and stored in the hash map
"""

class Solution:
    def __init__(self, nums: list[int], k: int) -> None:
        self.nums = nums
        self.k = k
    
    def contains_nearby_duplicate(self) -> bool:
        """Return True if there are duplicates within distance k, False otherwise."""
        seen = {}
        
        for i, num in enumerate(self.nums):
            # If we've seen this number before and it's within k positions
            if num in seen and i - seen[num] <= self.k:
                return True
            else:
                seen[num] = i
        return False

# Test cases
test1 = Solution([1, 2, 3, 1], 3)
print(f"Test 1: {test1.contains_nearby_duplicate()}")  # Expected: True

test2 = Solution([1, 0, 1, 1], 1)
print(f"Test 2: {test2.contains_nearby_duplicate()}")  # Expected: True

solution3 = Solution([1, 2, 3, 1, 2, 3], 2)
print(f"Test 3: {solution3.contains_nearby_duplicate()}")  # Expected: False

solution4 = Solution([99, 99], 2)
print(f"Test 4: {solution4.contains_nearby_duplicate()}")  # Expected: True

solution5 = Solution([1, 2, 3, 4, 5], 3)
print(f"Test 5: {solution5.contains_nearby_duplicate()}")  # Expected: False

solution6 = Solution([], 0)
print(f"Test 6: {solution6.contains_nearby_duplicate()}")  # Expected: False

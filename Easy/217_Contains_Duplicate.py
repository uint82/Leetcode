"""
Problem #217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Approach:
- Convert the array to a set, which removes all duplicates.
- Compare the length of the set with the original array.
- If the lengths are different, it means there were duplicates in the original array.

Time Complexity: O(n) — processing each element once
Space Complexity: O(n) — storing up to n elements in the set
"""

class Solution:

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def contains_duplicate(self) -> bool:
        """Return true if any value appears at least twice in the array, false otherwise."""
        return len(self.nums) != len(set(self.nums))


# Test cases
solution1 = Solution([1, 2, 3, 1])
print(f"Test 1: {solution1.contains_duplicate()}")  # Expected: True

solution2 = Solution([1, 2, 3, 4])
print(f"Test 2: {solution2.contains_duplicate()}")  # Expected: False

solution3 = Solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(f"Test 3: {solution3.contains_duplicate()}")  # Expected: True

solution4 = Solution([])
print(f"Test 4: {solution4.contains_duplicate()}")  # Expected: False

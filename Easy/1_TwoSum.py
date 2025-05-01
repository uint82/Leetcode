"""
Problem #1: Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Approach:
- Use a hash map to store the value and its index while iterating.
- For each number, compute its complement (target - number).
- If the complement exists in the hash map, return the indices.
- Otherwise, add the current number and its index to the hash map.

Time Complexity: O(n) — one pass through the list
Space Complexity: O(n) — storing up to n elements in the hash map
"""

class Solution:
    def __init__(self, nums: list[int], target: int) -> None:
        self.nums = nums
        self.target = target

    def two_sum(self) -> list[int]:
        """Return indices of two numbers in the list that add up to the target."""
        num_map = {}

        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []  # No valid pair found

# Test cases
solution1 = Solution([2, 7, 11, 15], 9)
print(f"Test 1: {solution1.two_sum()}")  # Expected: [0, 1]

solution2 = Solution([3, 2, 4], 6)
print(f"Test 2: {solution2.two_sum()}")  # Expected: [1, 2]

solution3 = Solution([3, 3], 6)
print(f"Test 3: {solution3.two_sum()}")  # Expected: [0, 1]

solution4 = Solution([1, 2, 3, 4, 5], 10)
print(f"Test 4: {solution4.two_sum()}")  # Expected: [] (no solution)

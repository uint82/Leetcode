"""
Problem #268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example:
Input: nums = [3,0,1]
Output: 2

Approach:
- Use the mathematical formula for the sum of first n natural numbers: n*(n+1)/2
- Calculate the expected sum of numbers from 0 to n (where n is the length of the array)
- Calculate the actual sum of the numbers in the array
- The difference between the expected sum and actual sum is the missing number

Time Complexity: O(n) — one pass through the array to calculate the sum
Space Complexity: O(1) — using only a constant amount of extra space
"""

class Solution:

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def missing_number(self) -> int:
        """Return the missing number in the range [0, n] from the array."""
        n = len(self.nums)

        expected_sum = n * (n + 1) // 2    
        actual_sum = sum(self.nums)
        return expected_sum - actual_sum


# Test cases
solution1 = Solution([3, 0, 1])
print(f"Test 1: {solution1.missing_number()}")  # Expected: 2

solution2 = Solution([0, 1])
print(f"Test 2: {solution2.missing_number()}")  # Expected: 2

solution3 = Solution([9, 6, 4, 2, 3, 5, 7, 0, 1])
print(f"Test 3: {solution3.missing_number()}")  # Expected: 8

solution4 = Solution([0])
print(f"Test 4: {solution4.missing_number()}")  # Expected: 1

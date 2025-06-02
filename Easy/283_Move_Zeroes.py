"""
Problem #283: Move Zeroes

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Approach:
- Use a two-pointer technique with one pointer (`non_zero_pointer`) tracking the position to place the next non-zero element.
- Iterate through the array:
    - If the current element is non-zero, swap it with the element at `non_zero_pointer`.
    - Increment `non_zero_pointer` if a non-zero is placed.
- This ensures non-zero elements retain order, and zeroes are moved to the end.

Time Complexity: O(n) — single pass through the array
Space Complexity: O(1) — in-place with constant space
"""

class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def moveZeroes(self) -> None:
        non_zero_pointer = 0
        n = len(self.nums)
        for i in range(n):
            if self.nums[i] != 0:
                if i != non_zero_pointer:
                    self.nums[non_zero_pointer], self.nums[i] = self.nums[i], self.nums[non_zero_pointer]
                non_zero_pointer += 1

# Test cases
# Test case 1: Example 1
solution1 = Solution([0, 1, 0, 3, 12])
solution1.moveZeroes()
print(f"Test 1: {solution1.nums}")  # Expected: [1, 3, 12, 0, 0]

# Test case 2: Example 2
solution2 = Solution([0])
solution2.moveZeroes()
print(f"Test 2: {solution2.nums}")  # Expected: [0]

# Test case 3: Additional test
solution3 = Solution([4, 0, 1, 0, 3, 12])
solution3.moveZeroes()
print(f"Test 3: {solution3.nums}")  # Expected: [4, 1, 3, 12, 0, 0]

# Test case 4: No zeros
solution4 = Solution([1, 2, 3, 4])
solution4.moveZeroes()
print(f"Test 4: {solution4.nums}")  # Expected: [1, 2, 3, 4]

# Test case 5: All zeros
solution5 = Solution([0, 0, 0])
solution5.moveZeroes()
print(f"Test 5: {solution5.nums}")  # Expected: [0, 0, 0]

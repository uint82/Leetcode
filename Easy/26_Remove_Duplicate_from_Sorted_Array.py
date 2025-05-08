"""
Problem #26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
- The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Approach:
- Use a two-pointer technique: one pointer tracks the position for the next unique element, the other iterates through the array.
- Start with k = 1 (assuming the first element is already in place).
- Iterate through the array starting from index 1.
- When a new unique element is found (different from the previous element), place it at position k and increment k.
- Return k as the count of unique elements.

Time Complexity: O(n) — one pass through the array
Space Complexity: O(1) — in-place algorithm with constant extra space
"""

class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def remove_duplicates(self) -> int:
        """Remove duplicates in-place and return the count of unique elements."""
        if not self.nums:
            return 0

        k = 1  

        for i in range(1, len(self.nums)):
            if self.nums[i - 1] != self.nums[i]:
                self.nums[k] = self.nums[i]  
                k += 1
        
        return k

# Test cases
solution1 = Solution([1, 1, 2])
k1 = solution1.remove_duplicates()
print(f"Test 1: k = {k1}, nums = {solution1.nums[:k1]}")  # Expected: k = 2, nums = [1, 2]

solution2 = Solution([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
k2 = solution2.remove_duplicates()
print(f"Test 2: k = {k2}, nums = {solution2.nums[:k2]}")  # Expected: k = 5, nums = [0, 1, 2, 3, 4]

solution3 = Solution([1, 2, 3, 4, 5])
k3 = solution3.remove_duplicates()
print(f"Test 3: k = {k3}, nums = {solution3.nums[:k3]}")  # Expected: k = 5, nums = [1, 2, 3, 4, 5]

solution4 = Solution([])
k4 = solution4.remove_duplicates()
print(f"Test 4: k = {k4}, nums = {solution4.nums[:k4] if k4 > 0 else []}")  # Expected: k = 0, nums = []

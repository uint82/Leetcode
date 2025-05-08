"""
Problem #27: Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
- The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Approach:
- Use a two-pointer technique: one pointer (k) to track where to place the next element that isn't equal to val,
  and the other pointer (i) to iterate through the array.
- For each element, if it's not equal to val, place it at position k and increment k.
- Return k as the count of elements not equal to val.

Time Complexity: O(n) — one pass through the array
Space Complexity: O(1) — in-place algorithm with constant extra space
"""

class Solution:
    def __init__(self, nums: list[int], val: int) -> None:
        self.nums = nums
        self.val = val

    def remove_element(self) -> int:
        """Remove all occurrences of val in-place and return the count of elements not equal to val."""
        k = 0

        for i in range(len(self.nums)):
            if self.nums[i] != self.val:
                self.nums[k] = self.nums[i]
                k += 1
        
        return k

# Test cases
solution1 = Solution([3, 2, 2, 3], 3)
k1 = solution1.remove_element()
print(f"Test 1: k = {k1}, nums = {solution1.nums[:k1]}")  # Expected: k = 2, nums = [2, 2]

solution2 = Solution([0, 1, 2, 2, 3, 0, 4, 2], 2)
k2 = solution2.remove_element()
print(f"Test 2: k = {k2}, nums = {solution2.nums[:k2]}")  # Expected: k = 5, nums = [0, 1, 3, 0, 4]

solution3 = Solution([1], 1)
k3 = solution3.remove_element()
print(f"Test 3: k = {k3}, nums = {solution3.nums[:k3] if k3 > 0 else []}")  # Expected: k = 0, nums = []

solution4 = Solution([], 1)
k4 = solution4.remove_element()
print(f"Test 4: k = {k4}, nums = {solution4.nums[:k4]}")  # Expected: k = 0, nums = []

solution5 = Solution([4, 4, 4, 4], 4)
k5 = solution5.remove_element()
print(f"Test 5: k = {k5}, nums = {solution5.nums[:k5] if k5 > 0 else []}")  # Expected: k = 0, nums = []

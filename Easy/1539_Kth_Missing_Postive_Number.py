"""
Problem #1539: Kth Missing Positive Number

Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`.

Return the kth positive integer that is missing from this array.

Example:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,...]. The 5th missing positive integer is 9.

Approach:
- Use binary search to efficiently find the kth missing positive number.
- For each index i, calculate how many positive integers are missing up to that position.
- The number of missing positives at index i is: arr[i] - (i + 1)
  (Since if no numbers were missing, arr[i] would equal i + 1)
- Once we find the position where k or more numbers are missing, we can calculate the kth missing number.

Time Complexity: O(log n) — binary search on the array of length n
Space Complexity: O(1) — using constant extra space
"""

class Solution:
    def __init__(self, arr: list[int], k: int) -> None:
        self.arr = arr
        self.k = k

    def find_kth_positive(self) -> int:
        """Return the kth missing positive integer."""
        left, right = 0, len(self.arr) - 1
        n = len(self.arr)

        while left <= right:
            mid = (left + right) // 2
            
            if self.arr[mid] - (mid + 1) >= self.k:
                n = mid
                right = mid - 1
            else:
                left = mid + 1
        return n + self.k

# Test cases
solution1 = Solution([2, 3, 4, 7, 11], 5)
print(f"Test 1: {solution1.find_kth_positive()}")  # Expected: 9

solution2 = Solution([1, 2, 3, 4], 2)
print(f"Test 2: {solution2.find_kth_positive()}")  # Expected: 6

solution3 = Solution([2, 3, 4, 7, 11], 1)
print(f"Test 3: {solution3.find_kth_positive()}")  # Expected: 1

solution4 = Solution([1, 3, 5, 7], 4)
print(f"Test 4: {solution4.find_kth_positive()}")  # Expected: 8

solution5 = Solution([2], 1)
print(f"Test 5: {solution5.find_kth_positive()}")  # Expected: 1

solution6 = Solution([3, 10], 5)
print(f"Test 6: {solution6.find_kth_positive()}")  # Expected: 7

solution6 = Solution([1, 5, 6, 7], 3)
print(f"Test 7: {solution6.find_kth_positive()}")  # Expected: 4

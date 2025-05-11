"""
Problem #1550: Three Consecutive Odds

Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

Example:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000

Approach:
- Iterate through the array and count consecutive odd numbers.
- If we find 3 consecutive odd numbers, return true.
- Otherwise, reset the counter when we encounter an even number.
- If we finish iterating and don't find 3 consecutive odds, return false.

Time Complexity: O(n) — one pass through the array
Space Complexity: O(1) — using constant extra space
"""

class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def three_consecutive_odds(self) -> bool:
        """Return true if there are three consecutive odd numbers in the array."""
        if len(self.arr) < 3:
            return False

        odd_count = 0

        for num in self.arr:
            if odd_count == 3:
                return True
                
            if num % 2 == 1:  
                odd_count += 1
            else:
                odd_count = 0
                
        return odd_count >= 3 

# Test cases
solution1 = Solution([2, 6, 4, 1])
print(f"Test 1: {solution1.three_consecutive_odds()}")  # Expected: False

solution2 = Solution([1, 2, 34, 3, 4, 5, 7, 23, 12])
print(f"Test 2: {solution2.three_consecutive_odds()}")  # Expected: True

solution3 = Solution([1, 3, 5])
print(f"Test 3: {solution3.three_consecutive_odds()}")  # Expected: True

solution4 = Solution([1, 3, 5, 2])
print(f"Test 4: {solution4.three_consecutive_odds()}")  # Expected: True

solution5 = Solution([2, 4, 6, 8])
print(f"Test 5: {solution5.three_consecutive_odds()}")  # Expected: False

solution6 = Solution([1, 3, 2, 1, 3, 5])
print(f"Test 6: {solution6.three_consecutive_odds()}")  # Expected: True (last three elements)

solution7 = Solution([])
print(f"Test 7: {solution7.three_consecutive_odds()}")  # Expected: False (empty array)

solution8 = Solution([1, 3])
print(f"Test 8: {solution8.three_consecutive_odds()}")  # Expected: False (too short)

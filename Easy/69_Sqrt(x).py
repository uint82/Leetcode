"""
Problem #69: Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in python or x ** 0.5.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Approach:
- Binary search can efficiently find the square root.
- We search in the range [0, x//2 + 1] for a number whose square equals x.
- If exact square isn't found, we return the floor of the square root.
- For very large inputs, limiting the search space improves efficiency.

Time Complexity: O(log n) — binary search halves the search space with each iteration
Space Complexity: O(1) — only a constant amount of space is used
"""

class Solution:
    def __init__(self, x: int) -> None:
        self.x = x

    def my_sqrt(self) -> int:
        """Return the square root of x rounded down to the nearest integer."""
        # Handle edge cases
        if self.x == 0 or self.x == 1:
            return self.x
        
        # Initialize binary search boundaries
        # We know sqrt(x) ≤ x/2 for x > 4, so we can optimize our search space
        left, right = 0, self.x // 2 + 1
        
        # Binary search
        while left <= right:
            middle = (left + right) // 2
            middle_squared = middle * middle
            
            if middle_squared == self.x:
                return middle
            elif middle_squared < self.x:
                left = middle + 1
            else:
                right = middle - 1
        
        # When we exit the loop, right is the integer square root of x
        return right

# Test cases
solution1 = Solution(4)
print(f"Test 1: {solution1.my_sqrt()}")  # Expected: 2

solution2 = Solution(8)
print(f"Test 2: {solution2.my_sqrt()}")  # Expected: 2

solution3 = Solution(0)
print(f"Test 3: {solution3.my_sqrt()}")  # Expected: 0

solution4 = Solution(1)
print(f"Test 4: {solution4.my_sqrt()}")  # Expected: 1

solution5 = Solution(16)
print(f"Test 5: {solution5.my_sqrt()}")  # Expected: 4

solution6 = Solution(2147483647)  # Max 32-bit integer
print(f"Test 6: {solution6.my_sqrt()}")  # Expected: 46340

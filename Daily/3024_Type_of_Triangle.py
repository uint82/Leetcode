"""
Problem #3024: Type of Triangle

Given an array of three integers representing the sides of a triangle, determine the type of triangle.

Return:
- "none" if the three sides cannot form a triangle
- "equilateral" if all three sides are equal
- "isosceles" if exactly two sides are equal
- "scalene" if all three sides are different

Triangle Inequality Rule: For three sides to form a triangle, the sum of any two sides must be greater than the third side.

Example:
Input: nums = [3, 4, 5]
Output: "scalene"

Approach:
- First check if the sides can form a valid triangle using the triangle inequality rule.
- Since we sorted or can assume the largest side is at index 2, we only need to check if a + b > c.
- Use a set to count unique values to determine the triangle type.
- 1 unique value = equilateral, 2 unique values = isosceles, 3 unique values = scalene.

Time Complexity: O(1) — constant operations
Space Complexity: O(1) — constant space for the set of at most 3 elements
"""

class Solution:

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def triangle_type(self) -> str:
        """Return the type of triangle formed by the three sides."""
        a, b, c = self.nums
        
        # we only had to check side c since its triangle rule
        if a + b <= c:
            return "none"

        # now we can use set to determine the type of triangle
        unique = len(set(self.nums))

        if unique == 1:
            return "equilateral"
        elif unique == 2:
            return "isosceles"
        else:
            return "scalene"

# Test cases
solution1 = Solution([3, 3, 3])
print(f"Test 1: {solution1.triangle_type()}")  # Expected: "equilateral"

solution2 = Solution([3, 4, 5])
print(f"Test 2: {solution2.triangle_type()}")  # Expected: "scalene"

solution3 = Solution([5, 5, 8])
print(f"Test 3: {solution3.triangle_type()}")  # Expected: "isosceles"

solution4 = Solution([1, 2, 10])
print(f"Test 4: {solution4.triangle_type()}")  # Expected: "none"

solution5 = Solution([8, 4, 5])
print(f"Test 5: {solution5.triangle_type()}")  # Expected: "scalene"

"""
Problem #118: Pascal's Triangle

Given an integer `numRows`, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Approach:
- Start with the first row [1].
- For each subsequent row, start and end with 1.
- Each middle element is the sum of the two elements above it from the previous row.
- Build each row by iterating through the previous row and summing adjacent elements.

Time Complexity: O(numRows²) — we generate numRows rows, each with increasing length
Space Complexity: O(numRows²) — storing the entire triangle
"""

class Solution:
    def __init__(self, numRows: int) -> None:
        self.numRows = numRows

    def generate(self) -> list[list[int]]:
        """Return the first numRows of Pascal's triangle."""
        if self.numRows == 0:
            return []

        result = [[1]]  # First row is always [1]

        for i in range(1, self.numRows):
            prev_row = result[i - 1]
            new_row = [1]  # Each row starts with 1

            # Calculate middle elements by summing adjacent elements from previous row
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)  # Each row ends with 1
            result.append(new_row)

        return result

# Test cases
solution1 = Solution(5)
print(f"Test 1: {solution1.generate()}")  # Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

solution2 = Solution(1)
print(f"Test 2: {solution2.generate()}")  # Expected: [[1]]

solution3 = Solution(0)
print(f"Test 3: {solution3.generate()}")  # Expected: []

solution4 = Solution(3)
print(f"Test 4: {solution4.generate()}")  # Expected: [[1],[1,1],[1,2,1]]

solution5 = Solution(8)
print(f"Test 5: {solution5.generate()}")  # Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1]]

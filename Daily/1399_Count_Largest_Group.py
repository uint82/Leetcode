"""
Problem #1399: Count Largest Group

You are given an integer `n`. Each number from 1 to n is grouped by the sum of its digits.

Return the number of groups that have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Approach:
- Calculate the digit sum for each number from 1 to n.
- Count how many numbers have each digit sum using an array.
- Find the maximum count among all digit sums.
- Return how many digit sums have this maximum count.

Time Complexity: O(n * log10(n)) — for each number, we calculate its digit sum
Space Complexity: O(1) — fixed size array for digit sums (max 37 for 4-digit numbers)
"""

class Solution:

    def __init__(self, n: int) -> None:
        self.n = n
    
    def count_largest_group(self) -> int:

        MAX_DIGIT_SUM = 37 # 9x4 = 36 since python use 0-indexed and digit sum start from 1 we add + 1 
        counts = [0] * MAX_DIGIT_SUM

        for i in range(1, self.n + 1):
            ds = sum(int(d) for d in str(i))
            counts[ds] += 1

        max_size = max(counts)
        return counts.count(max_size)

# Test cases
solution1 = Solution(13)
print(f"Test 1: {solution1.count_largest_group()}")  # Expected: 4

solution2 = Solution(2)
print(f"Test 2: {solution2.count_largest_group()}")  # Expected: 2

solution3 = Solution(15)
print(f"Test 3: {solution3.count_largest_group()}")  # Expected: 6

solution4 = Solution(24)
print(f"Test 4: {solution4.count_largest_group()}")  # Expected: 5

solution5 = Solution(1)
print(f"Test 5: {solution5.count_largest_group()}")  # Expected: 1

solution6 = Solution(9)
print(f"Test 6: {solution6.count_largest_group()}")  # Expected: 9

solution7 = Solution(10)
print(f"Test 7: {solution7.count_largest_group()}")  # Expected: 1

solution8 = Solution(100)
print(f"Test 8: {solution8.count_largest_group()}")  # Expected: 1

solution9 = Solution(50)
print(f"Test 9: {solution9.count_largest_group()}")  # Expected: 1

solution10 = Solution(999)
print(f"Test 10: {solution10.count_largest_group()}")  # Expected: 2

solution11 = Solution(1000)
print(f"Test 11: {solution11.count_largest_group()}")  # Expected: 2

class Solution:
    def __init__(self, nums: list[int], target: int) -> None:
        self.nums = nums
        self.target = target

    def two_sum(self) -> list[int]:
        """Return indices of two numbers in the list that add up to the target."""
        num_map = {}

        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []  # No valid pair found

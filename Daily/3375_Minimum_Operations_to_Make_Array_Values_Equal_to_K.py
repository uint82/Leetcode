# Daily on 9 April 2025
# in this problem we only need to get the unique element that is more than k
# because total operations increased when the h value changes
# so we can just count the unique element in nums that is more than k
# we will get the minimum operations needed

class Solution:
    
    def __init__(self, nums: list[int], k: int) -> None:
        self.nums = nums
        self.k = k

    def minOperations(self) -> int:

        # check if there is an element that less than k
        # return -1 if exist
        for num in self.nums:
            if num < self.k:
                return -1

        # check all element that is more than k and not seen yet
        # if it True. increment number of operations and set the num to True
        seen = [False] * 101 # 101 cause the constrain rule in leetcode
        operations = 0
        for num in self.nums:
            if num > self.k and not seen[num]:
                seen[num] = True
                operations += 1

        return operations

# Test
test1 = Solution([4, 5, 7, 8, 9], 3)
print(f"Test 1: {test1.minOperations()}")  # Should return 4 (unique nums > 3: 4,5,7,8,9)

test2 = Solution([2, 5, 7, 8, 9], 3)
print(f"Test 2: {test2.minOperations()}")  # Should return -1 (2 is < 3)

test3 = Solution([5, 5, 5, 7, 7], 3)
print(f"Test 3: {test3.minOperations()}")  # Should return 2 (unique nums > 3: 5,7)

test4 = Solution([10, 10, 10], 5)
print(f"Test 4: {test4.minOperations()}")  # Should return 1 (unique nums > 5: 10)


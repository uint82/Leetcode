class Solution:
    
    def __init__(self, nums: list[int], target: int) -> None:
        self.nums = nums
        self.target = target
    
    def twoSum(self) -> list[int]:
        # Create local variables
        nums = self.nums
        target = self.target

        # Create a hash map to store values and their indices
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(self.nums):
            # Calculate the complement we need to find
            complement = self.target - num
            
            # If the complement exists in the map, return its index and current index
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the current number and its index
            num_map[num] = i
        
        # If no solution is found, return empty list
        return []

# Test
test1 = Solution([2, 7, 11, 15], 9)
print(f"Test 1: {test1.twoSum()}")  # Should return [0, 1]

test2 = Solution([3, 2, 4], 6)
print(f"Test 2: {test2.twoSum()}")  # Should return [1, 2]

test3 = Solution([3, 3], 6)
print(f"Test 3: {test3.twoSum()}")  # Should return [0, 1]

test4 = Solution([1, 2, 3, 4, 5], 10)
print(f"Test 4: {test4.twoSum()}")  # Should return [] (no solution)

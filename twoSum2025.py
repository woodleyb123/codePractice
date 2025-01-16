from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for i, n in enumerate(nums):
            newDict[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in newDict and newDict[diff] != i:
                return [i, newDict[diff]]
    
print(Solution.twoSum(Solution, [3,4,5,6], 7))
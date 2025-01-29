from typing import List

class Solution:
    # Two Pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for i, n in enumerate(nums):
            newDict[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in newDict and newDict[diff] != i:
                return [i, newDict[diff]]
            
    # One Pass

    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map and map[diff] != i:
                return [map[diff], i]
            else:
                map[n] = i

    
print(Solution.twoSumOnePass(Solution, [3,4,5,6], 7))
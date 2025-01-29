from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        print(newSet)
        longestSequence = 1
        currentSequence = 1
        for num in newSet:
            if num - 1 in newSet:
                currentSequence += 1
                continue
            elif num + 1 not in newSet:
                currentSequence = 1
                longestSequence = 1
            else:
                currentSequence += 1
                print(currentSequence)
                if longestSequence < currentSequence:
                    longestSequence = currentSequence

        return longestSequence

print(Solution.longestConsecutive(Solution, [2,20,4,10,3,4,5]))
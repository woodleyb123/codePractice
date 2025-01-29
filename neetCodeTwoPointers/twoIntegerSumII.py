from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r <= len(numbers)-1 and l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1,r+1]
    
print(Solution.twoSum(Solution, [-5, -3, 0, 2, 4, 6, 8], 5))
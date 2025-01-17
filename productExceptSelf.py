from typing import List

class Solution:
    #Time complexity = O(n^2)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        allNums = nums
        for i, n in enumerate(nums):
            allNums.remove(n)
            mult = 1
            print(allNums)

            for newNum in allNums:
                mult = mult * newNum

            allNums.insert(i, n)
            output.append(mult)
        
        return output
    
    def productExceptSelfTwo(self, nums: List[int]) -> List[int]:

        size = len(nums)
        output = [1] * size

        for i, n in enumerate(nums):
            if i == 0:
                output[i] = n
            else:
                output[i] = output[i-1] * n

        nums.reverse()
        suffixVal = 1
        for i, n in enumerate(nums):
            trueIndex = size - i - 1
            if trueIndex == size:
                output[trueIndex] = output[trueIndex-1]
                suffixVal *= n
            elif trueIndex == 0:
                output[trueIndex] = suffixVal
            else:
                output[trueIndex] = output[trueIndex-1] * suffixVal
                suffixVal *= n

        return output

print(Solution.productExceptSelfTwo(Solution, [-1,2,3,4]))
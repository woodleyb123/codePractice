from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Put together a map of unique anagram keys
        anaMap = {}

        # i is the index, n is the string (1, cats)
        for i, n in enumerate(strs):

            letterList2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            # l is the letter, n is the full word
            for l in n:
                index = ord(l)-97
                letterList2[index] += 1
            
            newKey = '-'.join(map(str, letterList2))
            anaMap[newKey] = anaMap.get(newKey, []) + [n]

        return list(anaMap.values())
    
print(Solution.groupAnagrams(Solution, ["bdddddddddd","bbbbbbbbbbc"]))
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for i in nums:
            map[i] = map.get(i, 0) + 1
        
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_map.keys())[:k]

print(Solution.topKFrequent(Solution, [7,7], 1))
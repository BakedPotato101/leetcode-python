from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        noDupes = set()
        for i in nums:
            noDupes.add(i)
        return len(noDupes)
    
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
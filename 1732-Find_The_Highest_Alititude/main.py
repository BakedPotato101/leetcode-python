from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        altitudes = [0]
        for num in gain:
            current += num
            altitudes.append(current)
        altitudes.sort()
        return altitudes[int(len(altitudes)-1)]
    

s = Solution()

print(s.largestAltitude([1,2,-3,2,10]))
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))
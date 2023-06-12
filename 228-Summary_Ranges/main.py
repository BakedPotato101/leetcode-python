from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s,c,e = nums[0],nums[0], None
        out = []
        for i in nums[1:]:
            c += 1
            if i == c:
                e = i
            else:
                if not e:
                    out.append(str(s))
                else:
                    out.append(f"{s}->{e}")
                s,c,e = i,i,None
        if not e:
            out.append(str(s))
        else:
            out.append(f"{s}->{e}")
        return out





s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))
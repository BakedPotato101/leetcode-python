class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lowerBound = 0
        upperBound = len(needle)
        if upperBound == 1:
            if needle in haystack:
                return haystack.index(needle)
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[lowerBound:upperBound]:
                return lowerBound
            else:
                lowerBound += 1
                upperBound += 1
        return -1

    
s = Solution()
print(s.strStr("aaa", "aaa"))
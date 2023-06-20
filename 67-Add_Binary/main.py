from operator import add
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(add(int(a,2),int(b,2)))[2:]
    
s = Solution()
print(s.addBinary("101101","11011"))
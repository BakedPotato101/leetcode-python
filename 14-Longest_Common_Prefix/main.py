from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        charSet = set()
        charIndex = 0
        check = True
        commonPrefix = str()

        if len(strs) == 1:
                commonPrefix += str(strs[0])
                return commonPrefix
        
        while check:
            for string in strs:
                if len(string) == 0:
                     return ""
                try:
                    charSet.add(string[charIndex])
                except:
                     return commonPrefix
            if len(charSet) == 1:
                commonPrefix += charSet.pop()
                charSet.clear
                charIndex += 1
            elif len(charSet) > 1:
                check = False
        return commonPrefix
            

        
            

        

            

    

d = Solution()

print(d.longestCommonPrefix(["a", "ab"]))




    



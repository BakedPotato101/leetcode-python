from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        charStack = []
        index = 0
        finalOut = ""
        numberOfstrs = len(strs)
        check = 0
        for string in strs:
            if not charStack:
                charStack.append(string[index])
            elif charStack[index] == string[index]:
                check += 1
            elif charStack[index] != string[index]:
                check = 
            else:
                index += 1
        return charStack
    

d = Solution()

d.longestCommonPrefix(["flower","flow","flight"])




    



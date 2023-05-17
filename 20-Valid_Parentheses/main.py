class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        if len(s) % 2 == 1:
            return False
        sList = list(s)
        index = 0 
        for item in sList:
            if item in valids:
                
            index += 1
                
        

d = Solution()

d.isValid("(){}[]")

        

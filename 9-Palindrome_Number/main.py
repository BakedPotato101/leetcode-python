class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_list = [*str(x)]
        rev_list.reverse()
        final = ''.join(rev_list)
        if final == str(x):
            return True
        else:
            return False
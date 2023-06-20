class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        three = 1
        for i in range(n-1):
            three = one + two
            one = two
            two = three
        return three
            


            
s = Solution
print(s.climbStairs(1,50))
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            one, two, three, new = 1, 0, 0, 1
            for i in range(n-1):
                new = one + two + three
                three = two
                two = one
                one = new
            return new
        
s = Solution()
print(s.tribonacci(1))
print(s.tribonacci(2))
print(s.tribonacci(3))
print(s.tribonacci(4))
print(s.tribonacci(5))

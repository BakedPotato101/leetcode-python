from typing import List

def incrementIndex(index, digits):
        new = digits[index] + 1
        digits.pop(index)
        digits.insert(index, new)
        return digits

def indexToZero(index, digits):
    digits.pop(index)
    digits.insert(index, 0)
    return digits

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = incrementIndex(int(len(digits))-1, digits)
        while 10 in digits:
            ten_location = digits.index(10)
            next_place_value = ten_location - 1
            if ten_location == 0:
                length = len(digits)
                digits.clear()
                digits.append(1)
                for i in range(length):
                     digits.append(0)
                return digits
            digits = incrementIndex(next_place_value, digits)
            digits = indexToZero(ten_location, digits)
        return digits
    
s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([9,9,9,9]))
print(s.plusOne([1,2,2,2,9,1,9]))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current_index = 0
        inner_index = 0
        for number in nums:
            for i in nums:
                if current_index != inner_index:
                    if (number + i) == target:
                        final = [current_index, inner_index]
                        return final
                inner_index += 1
            current_index += 1
            inner_index = 0

                

# [3, 2, 4]
                
            
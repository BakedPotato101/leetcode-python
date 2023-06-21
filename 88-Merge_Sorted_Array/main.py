from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = nums1[0:m]
        nums2 = nums2[0:n]
        i = 0
        while len(nums1) < n+m:
            to_insert = nums2[i]
            if to_insert in nums1:
                where = nums1.index(to_insert)
                nums1.insert(where, to_insert)
                i += 1
                print(f"inserted {to_insert} at index {where}")
            else:
                nums1.append(to_insert)
                i += 1
                print(f"{to_insert} is not in the first array, appending it")
        nums1.sort()
        print(nums1)
        nums1 = nums1
s = Solution()
s.merge([1,1,2,2,3], 3, [5,5,1,1,3], 3)
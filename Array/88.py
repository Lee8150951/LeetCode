from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1

if __name__=="__main__":
  nums1 = [1, 2, 3, 0, 0, 0]
  nums2 = [2, 5, 6]
  m = 3
  n = 3
  method = Solution()
  answer = method.merge(nums1, m, nums2, n)
  print(answer)
from typing import List
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums_short = nums1 if len(nums1) < len(nums2) else nums2
    nums_long = nums1 if len(nums1) >= len(nums2) else nums2
    ans = list()
    for i in nums_short:
      if i in nums_long:
        nums_long.remove(i)
        ans.append(i)
    return ans
    
      
if __name__=="__main__":
  nums1 = [4, 9, 5]
  nums2 = [9, 4, 9, 8, 4]
  method = Solution()
  answer = method.intersect(nums1, nums2)
  print(answer)
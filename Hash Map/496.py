from typing import List
class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = list()
    for i in nums1:
      position = nums2.index(i) + 1
      if position < len(nums2):
        for j in range(position, len(nums2)):
          if nums2[j] > i:
            ans.append(nums2[j])
            break
        else:
          ans.append(-1)
      else:
        ans.append(-1)
    return ans



if __name__=="__main__":
  nums1 = [2, 4]
  nums2 = [1, 2, 3, 4]
  method = Solution()
  answer = method.nextGreaterElement(nums1, nums2)
  print(answer)
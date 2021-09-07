from typing import List
class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    answer = list()
    for i in set1:
      if i in set2:
        answer.append(i)
    return answer


if __name__=="__main__":
  nums1 = [1,2,2,1]
  nums2 = [2,2]
  method = Solution()
  answer = method.intersection(nums1, nums2)
  print(answer)
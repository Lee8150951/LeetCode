from typing import List
class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    numSet = set(nums)
    if len(numSet) < 3:
      return max(numSet)
    nums = sorted(numSet)
    return nums[-3]
    
      
if __name__=="__main__":
  nums = [2, 2, 3, 1]
  method = Solution()
  answer = method.thirdMax(nums)
  print(answer)
from typing import List
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)
      
if __name__=="__main__":
  nums = [9,6,4,2,3,5,7,0,1]
  method = Solution()
  answer = method.missingNumber(nums)
  print(answer)
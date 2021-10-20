from typing import List
class Solution:
  def minMoves(self, nums: List[int]) -> int:
    nums = sorted(nums)
    ans = 0
    for i in nums:
      ans += i - nums[0]
    return ans
      
if __name__=="__main__":
  nums = [1, 4, 9]
  method = Solution()
  answer = method.minMoves(nums)
  print(answer)
from typing import List
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    # 排序
    # nums.sort()
    # for i in range(len(nums) - 1):
    #   if nums[i] == nums[i + 1]:
    #     return True
    # return False
    
    # 哈希表
    table = dict()
    for i, num in enumerate(nums):
      if num in table:
        return True
      table[num] = i
    return False

      
if __name__=="__main__":
  nums = [1,2,3,4]
  method = Solution()
  answer = method.containsDuplicate(nums)
  print(answer)
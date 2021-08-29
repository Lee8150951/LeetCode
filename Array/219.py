from typing import List
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # 哈希表
    table = dict()
    for i, num in enumerate(nums):
      if num in table:
        if abs(table[num] - i) <= k:
          return True
      table[num] = i
    return False

      
if __name__=="__main__":
  nums = [1,0,1,1]
  k = 1
  method = Solution()
  answer = method.containsNearbyDuplicate(nums, k)
  print(answer)
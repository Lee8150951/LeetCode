from typing import List
from collections import Counter
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    # 哈希表（时间复杂度O(2n)）
    # numTable = dict()
    # for num in nums:
    #   if num in numTable:
    #     numTable[num] += 1
    #   else:
    #     numTable[num] = 1
    # for key, value in numTable.items():
    #   if value == max(numTable.values()):
    #     return key
    # return 0

    # 哈希表（通过counter实现）
    # counts = Counter(nums)
    # return max(counts.keys(), key = counts.get)

    # 排序
    nums.sort()
    return nums[len(nums) // 2]

if __name__=="__main__":
  nums = [2, 2, 3, 3, 3, 2, 2]
  method = Solution()
  answer = method.majorityElement(nums)
  print(answer)
from typing import List
class Solution:
  # 使用Hash
  # def distributeCandies(self, candyType: List[int]) -> int:
  #   candyTable = dict()
  #   for i in candyType:
  #     if i in candyTable:
  #       candyTable[i] += 1
  #     else:
  #       candyTable[i] = 1
  #   nums = len(candyType) // 2
  #   return min(nums, len(candyTable.keys()))

  # 使用set
  def distributeCandies(self, candyType: List[int]) -> int:
    candyNum = len(set(candyType))
    nums = len(candyType) // 2
    return min(nums, candyNum)


if __name__=="__main__":
  candyType = [1,5,2,2,3,3]
  method = Solution()
  answer = method.distributeCandies(candyType)
  print(answer)
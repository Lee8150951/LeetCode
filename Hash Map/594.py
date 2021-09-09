from typing import List
class Solution:
  # 哈希映射
  def findLHS(self, nums: List[int]) -> int:
    numDict = dict()
    numList = list()
    for i in nums:
      if i in numDict:
        numDict[i] += 1
      else:
        numDict[i] = 1
    for j in list(numDict.keys()):
      if j + 1 in list(numDict.keys()):
        numList.append(numDict[j] + numDict[j + 1])
    if len(numList) == 0:
      return 0
    return max(numList)


if __name__=="__main__":
  nums = [1, 3, 2, 2, 5, 2, 3, 7]
  method = Solution()
  answer = method.findLHS(nums)
  print(answer)
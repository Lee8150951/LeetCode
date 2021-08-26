from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      # hash表
      dictory = dict()
      for i, num in enumerate(numbers):
        if target - num in dictory:
          return [dictory[target - num] + 1, i + 1]
        dictory[num] = i
      return "Not Found"


if __name__=="__main__":
  numbers = [2, 7, 11, 15]
  target = 9
  method = Solution()
  answer = method.twoSum(numbers, target)
  print(answer)
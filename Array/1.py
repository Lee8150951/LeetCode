from typing import List
class Solution_Violence:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens):
            for j in range(i+1, lens):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class Solution_Hash:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Table = dict()
        numsList = enumerate(nums)
        for i, num in numsList:
            if target - num in Table:
                return [Table[target - num], i]
            Table[num] = i

if __name__=="__main__":
  nums = [1, 3, 5, 9, 12]
  target = 14
  method01 = Solution_Violence()
  method02 = Solution_Hash()
  answer01 = method01.twoSum(nums, target)
  print(answer01)
  answer02 = method02.twoSum(nums, target)
  print(answer02)
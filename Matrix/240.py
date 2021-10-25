from typing import List
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # 暴力解法
    for column in matrix:
      for i in column:
        if i == target:
          return True
    return False

if __name__=="__main__":
  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
  target = 0
  method = Solution()
  answer = method.searchMatrix(matrix, target)
  print(answer)
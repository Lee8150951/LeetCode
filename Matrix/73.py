from typing import List
class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 暴力解法
    zeroList = list()
    for column in range(len(matrix)):
      for row in range(len(matrix[column])):
        if matrix[column][row] == 0:
          zeroList.append([column, row])
    for i in zeroList:
      column, row = i[0], i[1]
      # 将一行都变为0
      matrix[column] = [0 for _ in range(len(matrix[column]))]
      # 将一列都变为0
      for j in matrix:
        j[row] = 0
    return matrix
            

if __name__=="__main__":
  matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
  method = Solution()
  answer = method.setZeroes(matrix)
  print(answer)
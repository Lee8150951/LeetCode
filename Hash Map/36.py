from typing import List
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # 暴力解法
    def checkSame(nums: List[str]) -> bool:
      numList = [i for i in nums if i.isnumeric()]
      numSet = set(numList)
      return len(numList) == len(numSet)
    
    for row in board: # 检查行式
      if checkSame(row) == False:
        return False
    
    for i in range(9): # 检查列式
      if checkSame([j[i] for j in board]) == False:
        return False

    for i in range(1, 9, 3): # 检查九宫格
      maxtrixes = [[], [], []]
      for j in range(9):
        flag = j // 3
        maxtrixes[flag].append(board[i - 1][j])
        maxtrixes[flag].append(board[i][j])
        maxtrixes[flag].append(board[i + 1][j])
      for maxtrix in maxtrixes:
        if checkSame(maxtrix) == False:
          return False
    return True
      
    

if __name__=="__main__":
  board = [["5","3",".",".","7",".",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]]
  method = Solution()
  answer = method.isValidSudoku(board)
  print(answer)
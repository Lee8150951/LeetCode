from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rst = [1]             
        for i in range(rowIndex):
            rst.append(1)
            for j in range(len(rst)-2, 0, -1):
                rst[j] = rst[j] + rst[j-1]
        return rst


if __name__=="__main__":
  rowIndex = 4
  method = Solution()
  answer = method.getRow(rowIndex)
  print(answer)
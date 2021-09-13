from typing import List
class Solution:
  def chalkReplacer(self, chalk: List[int], k: int) -> int:
      total = sum(chalk)
      k %= total
      res = -1
      for i, cnt in enumerate(chalk):
        if cnt > k:
          res = i
          break
        k -= cnt
      return res

if __name__=="__main__":
  chalk = [3,4,1,2]
  k = 25
  method = Solution()
  answer = method.chalkReplacer(chalk, k)
  print(answer)
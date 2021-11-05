from typing import List
from collections import defaultdict
class Solution:
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
    dp = defaultdict(int)
    for v in arr:
      dp[v] = dp[v - difference] + 1
    return max(dp.values())
      

if __name__=="__main__":
  arr = [3, 0, -3, 4, -4, 7, 6]
  difference = 3
  method = Solution()
  answer = method.longestSubsequence(arr, difference)
  print(answer)
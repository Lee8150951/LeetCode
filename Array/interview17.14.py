from typing import List
class Solution:
  def smallestK(self, arr: List[int], k: int) -> List[int]:
    arr.sort()
    return arr[:k]

if __name__=="__main__":
  arr = [1, 3, 5, 7, 2, 4, 6, 8]
  k = 4
  method = Solution()
  answer = method.smallestK(arr, k)
  print(answer)
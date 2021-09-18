class Solution:
  def canWinNim(self, n: int) -> bool:
    return n % 4 != 0


if __name__=="__main__":
  n = 4
  method = Solution()
  answer = method.canWinNim(n)
  print(answer)
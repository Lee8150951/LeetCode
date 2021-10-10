class Solution:
  def arrangeCoins(self, n: int) -> int:
    if n == 0:
      return 0
    column = 1
    while True:
      flag = ((1 + column) * column) / 2
      diff = n - flag
      if diff < column + 1:
        return column
      column += 1

if __name__=="__main__":
  n = 10000
  method = Solution()
  answer = method.arrangeCoins(n)
  print(answer)
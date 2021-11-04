class Solution:
  # def isPerfectSquare(self, num: int) -> bool:
  #   if num ** 0.5 % 1 == 0:
  #     return True
  #   return False

  def isPerfectSquare(self, num: int) -> bool:
    x = 1
    square = 1
    while square <= num:
      if square == num:
        return True
      x += 1
      square = x * x
    return False

if __name__=="__main__":
  num = 20
  method = Solution()
  answer = method.isPerfectSquare(num)
  print(answer)
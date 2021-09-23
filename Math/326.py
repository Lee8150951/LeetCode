class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    # 循环
    # while n > 1:
    #   n /= 3
    # if n == 1:
    #   return True
    # return False

    # 递归
    if n == 1:
      return True
    if n % 3 != 0:
      return False
    return self.isPowerOfThree(n // 3)

if __name__=="__main__":
  n = 9
  method = Solution()
  answer = method.isPowerOfThree(n)
  print(answer)
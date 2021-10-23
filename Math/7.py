class Solution:
  def reverse(self, x: int) -> int:
    if x < -(2 ** 31) or x > (2 ** 31) - 1:
      return 0
    x_string = str(x)
    ans = ""
    if x_string[0] == "-":
      x_string = x_string[1:] 
      for i in x_string:
        ans = i + ans
      ans = "-" + ans
    else:
      for i in x_string:
        ans = i + ans   
    ans = int(ans)
    if ans < -(2 ** 31) or ans > (2 ** 31) - 1:
      return 0
    return int(ans)


if __name__=="__main__":
  x = 1534236469
  method = Solution()
  answer = method.reverse(x)
  print(answer)
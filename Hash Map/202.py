class Solution:
  def isHappy(self, n: int) -> bool:
    # 递归
    def multiple(num, n):
      numStack.append(num)
      num = str(num)
      new_multi = 0
      for i in num:
        new_multi += int(i) ** 2
      if num == "1":
        res.append(True)
        return
      elif new_multi in numStack:
        res.append(False)
        return
      else:
        multiple(new_multi, n)
    numStack = []
    res = [False]
    multiple(n, n)
    return res[-1]
    

if __name__=="__main__":
  n = 13
  method = Solution()
  answer = method.isHappy(n)
  print(answer)
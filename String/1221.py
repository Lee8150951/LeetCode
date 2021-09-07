class Solution:
  def balancedStringSplit(self, s: str) -> int:
    # 栈
    # stack = list()
    # num = 0
    # for i in s:
    #   if i == "L":
    #     if stack.count("R") == stack.count("L") + 1:
    #       stack.clear()
    #       num += 1
    #     else:
    #       stack.append("L")
    #   elif i == "R":
    #     if stack.count("L") == stack.count("R") + 1:
    #       stack.clear()
    #       num += 1
    #     else:
    #       stack.append("R")
    # return num

    # 贪心算法
    ans, d = 0, 0
    for i in s:
      if i == "L":
        d += 1
      else:
        d -= 1
      if d == 0:
        ans += 1
    return ans

if __name__=="__main__":
  s = "RLRRRLLRLL"
  method = Solution()
  answer = method.balancedStringSplit(s)
  print(answer)
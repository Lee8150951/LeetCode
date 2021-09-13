from collections import Counter
class Solution:
  def checkValidString(self, s: str) -> bool:
    starStack = list()
    leftStack = list()
    for i in range(len(s)):
      if s[i] == "(":
        leftStack.append(i)
      if s[i] == "*":
        starStack.append(i)
      if s[i] == ")":
        if leftStack:
          leftStack.pop()
        elif starStack:
          starStack.pop()
        else:
          return False
    while starStack and leftStack:
      star = starStack.pop()
      left = leftStack.pop()
      if star < left:
        return False
    return not leftStack
    


if __name__=="__main__":
  s = "(*)"
  method = Solution()
  answer = method.checkValidString(s)
  print(answer)
class Solution:
  def isValid(self, s: str) -> bool:
    pairs = {
      ")" : "(", "]" : "[", "}" : "{"
    }
    if len(s) % 2 != 0:
      return False
    bracketStack = list()
    for i in s:
      if i in pairs:
        if not bracketStack or bracketStack[-1] != pairs[i]:
          return False
        bracketStack.pop()
      else:
        bracketStack.append(i)
    return not bracketStack


if __name__=="__main__":
  s = "(("
  method = Solution()
  answer = method.isValid(s)
  print(answer)
class Solution:
  # 暴力解法（利用两个循环将字符串转化为对应数字列表）
  # def isIsomorphic(self, s: str, t: str) -> bool:
  #   return self.transToNum(s) == self.transToNum(t)
  
  # def transToNum(self, string: str) -> list:
  #   strList = list()
  #   numList = list()
  #   for i in string:
  #     if i not in strList:
  #       strList.append(i)
  #     numList.append(strList.index(i))
  #   return numList

  def isIsomorphic(self, s: str, t: str) -> bool:
    for i in range(len(s)):
      if s.index(s[i]) != t.index(t[i]):
        return False
    return True


if __name__=="__main__":
  s = "abcdefghijklmnopqrstuvwxyzva"
  t = "abcdefghijklmnopqrstuvwxyzck"
  method = Solution()
  answer = method.isIsomorphic(s, t)
  print(answer)
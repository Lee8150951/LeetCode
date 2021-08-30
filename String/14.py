from typing import List
class Solution:
  # 横向扫描
  # def longestCommonPrefix(self, strs: List[str]) -> str:
  #   length = len(strs)
  #   i = 0
  #   while i < length - 1:
  #     strs[i + 1] = self.lcp(strs[i], strs[i + 1])
  #     i += 1
  #   return strs[length - 1]


  # def lcp(self, str1, str2) -> str:
  #   maxlength = min(len(str1), len(str2))
  #   answer = ""
  #   index = 0
  #   while index < maxlength:
  #     if str1[index] == str2[index]:
  #       answer = answer + str1[index]
  #     else:
  #       break
  #     index += 1
  #   return answer

  # 纵向扫描
  # def longestCommonPrefix(self, strs: List[str]) -> str:
  #   length, count = len(strs[0]), len(strs)
  #   for i in range(length):
  #     c = strs[0][i]
  #     if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
  #       return strs[0][:i]
  #   return strs[0]

  # 分治法
  def longestCommonPrefix(self, strs: List[str]) -> str:
    def lcp(start, end):
      if start == end:
        return strs[start]

      mid = (start + end) // 2
      lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
      minLength = min(len(lcpLeft), len(lcpRight))
      for i in range(minLength):
        if lcpLeft[i] != lcpRight[i]:
          return lcpLeft[:i]
          
      return lcpLeft[:minLength]

    return "" if not strs else lcp(0, len(strs) - 1)
      

if __name__=="__main__":
  strs = ["cir","car"]
  method = Solution()
  answer = method.longestCommonPrefix(strs)
  print(answer)
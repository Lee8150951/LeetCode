from typing import List
class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    # 暴力解法（超时）
    # ans = set()
    # if len(s) <= 10:
    #   return list(ans)
    # maxLength = len(s) - 9
    # for i in range(maxLength):
    #   target = s[i:i + 10]
    #   remain = s[i+1:]
    #   if target in remain:
    #     ans.add(target)
    # return list(ans)

    # 哈希表
    answer = set()
    dictory = dict()
    for i in range(len(s) - 9):
      target = s[i:i + 10]
      if target not in dictory:
        dictory[target] = 1
      else:
        answer.add(target)
    return list(answer)
    

if __name__=="__main__":
  s = "A"
  method = Solution()
  answer = method.findRepeatedDnaSequences(s)
  print(answer)
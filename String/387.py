from collections import Counter
class Solution:
  def firstUniqChar(self, s: str) -> int:
    # 手动写hash表，使用计数频率
    # strTable = dict()
    # for i in s:
    #   if i in strTable:
    #     strTable[i] +=1
    #   else:
    #     strTable[i] = 1
    # try:
    #   num = list(strTable.values()).index(1)
    #   alpha = list(strTable.keys())[num]
    #   return s.index(alpha)
    # except:
    #   return -1

    # 使用counter方法
    counts = Counter(s)
    for key, value in enumerate(s):
      if counts[value] == 1:
        return key
    return -1
    

if __name__=="__main__":
  s = "dddccdbba"
  method = Solution()
  answer = method.firstUniqChar(s)
  print(answer)
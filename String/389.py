class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    # 指针
    # sList = sorted([i for i in s])
    # tList = sorted([i for i in t])
    # for i in range(len(sList)):
    #   if sList[i] != tList[i]:
    #     return tList[i]
    # return tList[len(tList) - 1]

    # ASCII求和
    sSum = sum(map(ord, [i for i in s]))
    tSum = sum(map(ord, [i for i in t]))
    return chr(tSum - sSum)
    

if __name__=="__main__":
  s = "ae"
  t = "aea"
  method = Solution()
  answer = method.findTheDifference(s, t)
  print(answer)
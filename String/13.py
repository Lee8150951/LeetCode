class Solution:
  def romanToInt(self, s: str) -> int:
    # 暴力解法
    # stringList = list(s)
    # stringList.append(0)
    # i = j = 0
    # while i < len(stringList):
    #   t = stringList[i]
    #   if t == "I":
    #     stringList[i] = 1
    #   elif t == "V":
    #     stringList[i] = 5
    #   elif t == "X":
    #     stringList[i] = 10
    #   elif t == "L":
    #     stringList[i] = 50
    #   elif t == "C":
    #     stringList[i] = 100
    #   elif t == "D":
    #     stringList[i] = 500
    #   elif t == "M":
    #     stringList[i] = 1000
    #   i += 1
    # while j < len(stringList) - 1:
    #   if stringList[j] < stringList[j + 1]:
    #     stringList[j] = -stringList[j]
    #   j += 1
    # return sum(stringList)

    # 字典
    dictory = {
      "I" : 1, "V" : 5, "X" : 10,
      "L" : 50, "C" : 100, "D" : 500,
      "M" : 1000, "Z" : 0
    }
    stringList = list(s)
    stringList.append("Z")
    i = 0
    while i < len(stringList) - 1:
      stringList[i] = dictory[stringList[i]]
      nextValue = dictory[stringList[i + 1]]
      if stringList[i] < nextValue:
        stringList[i] = - stringList[i]
      i += 1
    stringList.pop()
    return sum(stringList)

if __name__=="__main__":
  s = "DXX"
  method = Solution()
  answer = method.romanToInt(s)
  print(answer)
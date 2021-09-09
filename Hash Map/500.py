from typing import List
class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    keyboardTable = [
      "qwertyuiopQWERTYUIOP",
      "asdfghjklASDFGHJKL",
      "zxcvbnmZXCVBNM"
    ]
    ans = []
    for word in words:
      positionList = ""
      for i in word:
        for j in range(len(keyboardTable)):
          if i in keyboardTable[j]:
            positionList += str(j)
      if positionList.count(positionList[0]) == len(word):
        ans.append(word)
    return ans



if __name__=="__main__":
  words = ["Hello", "Alaska", "Dad", "Peace"]
  method = Solution()
  answer = method.findWords(words)
  print(answer)
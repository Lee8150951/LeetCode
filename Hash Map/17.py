from typing import List
class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if digits == "":
      return []
    dictory = {
      2 : "abc", 3 : "def", 4 : "ghi",
      5 : "jkl", 6 : "mno", 7 : "pqrs",
      8 : "tuv", 9 : "wxyz"
    }
    def backtrack(combination, nextdigit: str):
      if nextdigit == "":
        res.append(combination)
      else:
        searchString = dictory[int(nextdigit[0])]
        for i in searchString:
          backtrack(combination + i, nextdigit[1:])
    res = []
    backtrack("", digits)
    return res

if __name__=="__main__":
  digits = "23"
  method = Solution()
  answer = method.letterCombinations(digits)
  print(answer)
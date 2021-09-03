class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rList, mList = list(ransomNote), list(magazine)
    for i in rList:
      if i in mList:
        mList.remove(i)
      else:
        return False
    return True


if __name__=="__main__":
  ransomNote = "aa"
  magazine = "ab"
  method = Solution()
  answer = method.canConstruct(ransomNote, magazine)
  print(answer)
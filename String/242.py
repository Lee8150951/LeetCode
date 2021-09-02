class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__=="__main__":
  s = "rat"
  t = "car"
  method = Solution()
  answer = method.isAnagram(s, t)
  print(answer)
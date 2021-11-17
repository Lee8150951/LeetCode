from typing import List
from typing import DefaultDict
class Solution:
  def maxProduct(self, words: List[str]) -> int:
    def hashset(word):
      # 用26位位运算表示二十六个字母在word中被使用的情况
      return sum(1 << (ord(c) - ord('a')) for c in set(word))
    d, ans = DefaultDict(int), 0
    for w in words:
      h = hashset(w)
      if d[h] < len(w):
        for other in d:
          # 如果位运算&的结果为0，说明他们没有使用过同样的字母，可以计算答案
          if not other & h:
            ans = max(d[other] * len(w), ans)
        d[h] = len(w)
    return ans
          
          
          
if __name__=="__main__":
  words = ["abcw","baz","foo","bar","xtfn","abcdef"]
  method = Solution()
  answer = method.maxProduct(words)
  print(answer)
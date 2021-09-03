from typing import List
class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
      Do not return anything, modify s in-place instead.
    """
    # 调用reverse()方法
    # s.reverse()
    # return s

    # 交换赋值
    i = 0
    while i < len(s) // 2:
      s[i], s[-i - 1] = s[-i - 1], s[i]
      i += 1
    return s

if __name__=="__main__":
  s = ["h","e","l","l","o"]
  method = Solution()
  answer = method.reverseString(s)
  print(answer)
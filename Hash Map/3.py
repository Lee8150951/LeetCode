class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # 自写方法，存储数组，不断检测前一个数组中是否出现相同字符
    # 如果出现则斩断并append现有字符
    # slist = [[]]
    # for i in s:
    #   if i not in slist[-1]:
    #     slist[-1].append(i)
    #   else:
    #     newlist = slist[-1][slist[-1].index(i) + 1:]
    #     newlist.append(i)
    #     slist.append(newlist)
    # return slist

    # 滑动窗口
    occ = set()
    n = len(s)
    rk, ans = -1, 0
    for i in range(n):
      if i != 0:
        occ.remove(s[i - 1])
      while rk + 1 < n and s[rk + 1] not in occ:
        occ.add(s[rk + 1])
        rk += 1
      ans = max(ans, rk - i + 1)
    return ans


if __name__=="__main__":
  s = "abcabcbb"
  method = Solution()
  answer = method.lengthOfLongestSubstring(s)
  print(answer)
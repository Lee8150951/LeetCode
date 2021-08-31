class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    # 暴力解法
    # index = 0
    # length = len(needle)
    # if length == 0:
    #   return 0
    # while index < len(haystack):
    #   if index + length - 1 < len(haystack):
    #     if haystack[index : index + length] == needle:
    #       return index
    #   else:
    #     return -1
    #   index += 1
    # return -1

    return haystack.find(needle)


if __name__=="__main__":
  haystack = "hello"
  needle = ""
  method = Solution()
  answer = method.strStr(haystack, needle)
  print(answer)
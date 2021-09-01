from itertools import zip_longest
class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    # 暴力解法
    # v1_list = version1.split('.')
    # v2_list = version2.split('.')
    # length = min(len(v1_list), len(v2_list))
    # for i in range(length):
    #   if int(v1_list[i]) > int(v2_list[i]):
    #     return 1
    #   if int(v1_list[i]) < int(v2_list[i]):
    #     return -1
    # if len(v1_list) != length and any(int(i) > 0 for i in v1_list[length:]):
    #   return 1
    # if len(v2_list) != length and any(int(i) > 0 for i in v2_list[length:]):
    #   return -1
    # return 0

    # 使用zip_longest方法直接分割检索
    # versionList = zip_longest(version1.split('.'), version2.split('.'), fillvalue="0")
    # for i, j in list(versionList):
    #   x, y = int(i), int(j)
    #   if x > y:
    #     return 1
    #   elif x < y:
    #     return -1
    # return 0

    # 双指针
    n, m = len(version1), len(version2)
    i, j = 0, 0
    while i < n or j < m:
      x = 0
      while i < n and version1[i] != '.':
        x = x * 10 + ord(version1[i]) - ord('0')
        i += 1
      i += 1  # 跳过点号
      y = 0
      while j < m and version2[j] != '.':
        y = y * 10 + ord(version2[j]) - ord('0')
        j += 1
      j += 1  # 跳过点号
      if x != y:
        return 1 if x > y else -1
    return 0
      

if __name__=="__main__":
  version1 = "1.0.1"
  version2 = "1"
  method = Solution()
  answer = method.compareVersion(version1, version2)
  print(answer)
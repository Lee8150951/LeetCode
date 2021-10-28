class Solution:
  def reorderedPowerOf2(self, n: int) -> bool:
    array = sorted([i for i in str(n)])
    targets = list()
    flag = 0
    while True:
      target = 2 ** flag
      if len(str(target)) <= len(array):
        targetArray = sorted([i for i in str(target)])
        targets.append(targetArray)
        flag += 1
      else:
        break
    if array in targets:
      return True
    else:
      return False


if __name__=="__main__":
  n = 46
  method = Solution()
  answer = method.reorderedPowerOf2(n)
  print(answer)
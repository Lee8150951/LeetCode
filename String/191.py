class Solution:
  def hammingWeight(self, n: int) -> int:
    ret = sum(1 for i in range(32) if n & (1 << i)) 
    return ret


if __name__=="__main__":
  n = 1011
  method = Solution()
  answer = method.hammingWeight(n)
  print(answer)
class Solution:
  def reverseBits(self, n: int) -> int:
    string = str(bin(n))
    answer = string[::-1][0:-2].ljust(32, "0")
    return int(answer, 2)


if __name__=="__main__":
  n = 0b00000010100101000001111010011100
  method = Solution()
  answer = method.reverseBits(n)
  print(answer)
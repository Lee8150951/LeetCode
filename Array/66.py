from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        for i in digits:
            result = result + str(i)
        result = [int(i) for i in str(int(result) + 1)]
        return list(result)

if __name__=="__main__":
  digits = [4, 3, 2, 1]
  method = Solution()
  answer = method.plusOne(digits)
  print(answer)
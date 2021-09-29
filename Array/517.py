from typing import List
class Solution:
  def findMinMoves(self, machines: List[int]) -> int:
    machineSum = sum(machines)
    if machineSum % len(machines) != 0:
      return -1
    avg = machineSum // len(machines)
    ans, s = 0, 0
    for num in machines:
      num -= avg
      s += num
      ans = max(ans, abs(s), num)
    return ans

if __name__=="__main__":
  machines = [4, 0, 0, 4]
  method = Solution()
  answer = method.findMinMoves(machines)
  print(answer)
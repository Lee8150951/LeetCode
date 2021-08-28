from typing import List
class Solution:
  def countPrimes(self, n: int) -> int:
    # 暴力解法（超时）
    # count = 0
    # if n <= 1:
    #     return count
    # else:
    #   for num in range(2, n):
    #     for i in range(2, num):
    #       if num % i == 0:
    #         break
    #     else:
    #       count += 1
    # return count

    # 列表法（超时）
    # numList = [i for i in range(n)]
    # multiList = list()
    # count = 0
    # index = 2
    # while index < len(numList):
    #   num = numList[index]
    #   maxMulti = numList[n - 1] // num
    #   multi = [i for i in range(2, maxMulti + 1)]
    #   for i in multi:
    #     multiList.append(num * i)
    #   if num not in multiList:
    #     count += 1
    #   index += 1
    # return count

    # 自己写的筛选法（超时）
    # numList = [i for i in range(n)]
    # lenght = len(numList)
    # index = 2
    # while index < lenght:
    #   num = numList[index]
    #   maxMulti = numList[lenght - 1] // num
    #   multi = [i for i in range(2, maxMulti + 1)]
    #   for i in multi:
    #     if num * i in numList:
    #       numList.remove(num * i)
    #   lenght = len(numList)
    #   index += 1
    # if n <= 1:
    #   return 0
    # else:
    #   return len(numList) - 2

    # 埃氏筛
    is_prime = [0, 0] + [1 for _ in range(2, n)]
    prescribe = int(n ** 0.5)
    for i in range(2, prescribe + 1):
      if is_prime[i]:
        for j in range(i * i, n, i):
          is_prime[j] = 0
    return sum(is_prime)
      
if __name__=="__main__":
  n = 1000
  method = Solution()
  answer = method.countPrimes(n)
  print(answer)
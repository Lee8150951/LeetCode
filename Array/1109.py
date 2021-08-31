from typing import List
class Solution:
  def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    # 暴力解法（超时）
    # answer = list()
    # reserve = dict()
    # for flight in bookings:
    #   first = flight[0]
    #   last = flight[1]
    #   value = flight[2]
    #   for i in range(first, last + 1):
    #     if i in reserve:
    #       reserve[i] = reserve[i] + value
    #     else:
    #       reserve[i] = value
    # for i in range(1, n + 1):
    #   if i in reserve:
    #     answer.append(reserve[i])
    #   else:
    #     answer.append(0)
    # return answer

    # 差分法
    difList = [0 for _ in range(n + 1)]
    for first, last, seats in bookings:
      difList[first - 1] += seats
      difList[last] -= seats
    
    for i in range(n):
      difList[i + 1] += difList[i]
    return difList[:n]

if __name__=="__main__":
  bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
  n = 5
  method = Solution()
  answer = method.corpFlightBookings(bookings, n)
  print(answer)
from utils import ListNode
from typing import List
from utils import create_linked_list
class Solution:
  def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
    cur = head
    length = 0
    while cur:
      length += 1
      cur = cur.next
    basiclLength = length // k
    remain = length % k
    answer = [None] * k
    point = head
    index = 0
    while point:
      answer[index] = point
      last = None
      cur_length = basiclLength + 1 if index < remain else basiclLength
      for i in range(cur_length):
        last = point
        point = point.next
      last.next = None
      index += 1
    return answer



if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  k = 5
  method = Solution()
  answer = method.splitListToParts(head, k)
  print(answer)
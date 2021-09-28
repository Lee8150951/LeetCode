from utils import ListNode
from utils import create_linked_list
from typing import List
class Solution:
  def reversePrint(self, head: ListNode) -> List[int]:
    cur = head
    array = list()
    while cur:
      array.append(cur.val)
      cur = cur.next
    return array[::-1]

if __name__=="__main__":
  head = create_linked_list([1, 3, 2])
  method = Solution()
  answer = method.reversePrint(head)
  print(answer)
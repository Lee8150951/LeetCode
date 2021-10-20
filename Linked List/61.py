from utils import ListNode
from utils import create_linked_list
from typing import Optional
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head == None:
      return None
    # 获得长度，形成换装链表
    point_01 = head
    length = 1
    while point_01.next:
      length += 1
      point_01 = point_01.next
    point_01.next = head
    # 斩断链表
    k = k % length
    current = length - k
    point_02 = head
    for _ in range(current - 1):
      point_02 = point_02.next
    answer = point_02.next
    point_02.next = None
    return answer
    

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5])
  k = 2
  val = 6
  method = Solution()
  answer = method.rotateRight(head, k)
  print(answer)
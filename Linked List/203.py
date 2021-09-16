from utils import ListNode
from utils import create_linked_list
class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    cur = ListNode()
    cur.next = head
    point = cur
    while point:
      if point.next and point.next.val == val:
        point.next = point.next.next
      else:
        point = point.next
    return cur.next


if __name__=="__main__":
  head = create_linked_list([1,2,6,3,4,5,6])
  val = 6
  method = Solution()
  answer = method.removeElements(head, val)
  print(answer)
from utils import ListNode
from utils import create_linked_list
class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    p = less = ListNode(0)
    q = more = ListNode(0)
    while head:
      if head.val < x:
        less.next = head
        less = less.next
      else:
        more.next = head
        more=more.next
      head = head.next
    more.next = None
    less.next = q.next
    return p.next


if __name__=="__main__":
  head = create_linked_list([1, 4, 3, 2, 5, 2])
  x = 3
  method = Solution()
  answer = method.partition(head, x)
  print(answer)
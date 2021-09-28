from utils import ListNode
from utils import create_linked_list
class Solution:
  def deleteNode(self, head: ListNode, val: int) -> ListNode:
    if head.val == val:
      return head.next
    pre, cur = head, head.next
    while cur and cur.val != val:
      pre, cur = cur, cur.next
    if cur:
      pre.next = cur.next
    return head

if __name__=="__main__":
  head = create_linked_list([4, 5, 1, 9])
  val = 5
  method = Solution()
  answer = method.deleteNode(head, val)
  print(answer)
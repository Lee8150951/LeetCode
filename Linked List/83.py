from utils import ListNode
from utils import create_linked_list
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
      return head
    cur = head
    while cur.next:
      if cur.val == cur.next.val:
        cur.next = cur.next.next
      else:
        cur = cur.next
    return head
        

if __name__=="__main__":
  head = create_linked_list([1, 1, 2])
  method = Solution()
  answer = method.deleteDuplicates(head)
  print(answer)
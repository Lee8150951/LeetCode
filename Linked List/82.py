from utils import ListNode
from utils import create_linked_list
class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
      return head
    ansHead = ListNode(0)
    ansHead.next = head
    cur = ansHead
    while cur.next and cur.next.next:
      if cur.next.val == cur.next.next.val:
        flag = cur.next.val
        while cur.next and cur.next.val == flag:
          cur.next = cur.next.next
      else:
        cur = cur.next
    return ansHead.next


if __name__=="__main__":
  head = create_linked_list([1, 1, 1, 2, 3])
  method = Solution()
  answer = method.deleteDuplicates(head)
  print(answer)
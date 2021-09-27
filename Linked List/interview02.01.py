from utils import ListNode
from utils import create_linked_list
class Solution:
  def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    numSet = {head.val}
    point = head
    while point.next:
      cur = point.next
      if cur.val not in numSet:
        numSet.add(cur.val)
        point = point.next
      else:
        point.next = point.next.next
    return head

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 3, 2, 1])
  method = Solution()
  answer = method.removeDuplicateNodes(head)
  print(answer)
from utils import ListNode
from utils import create_linked_list
class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
      return head
    first = head
    second = first.next
    head.next = None
    while second:
      cur = second.next
      second.next = first
      first = second
      second = cur
    return first


if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5])
  method = Solution()
  answer = method.reverseList(head)
  print(answer)
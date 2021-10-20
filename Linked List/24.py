from utils import ListNode
from utils import create_linked_list
class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    newHead = ListNode(0)
    newHead.next = head
    newLink = newHead
    while newLink.next and newLink.next.next:
      temp1 = newLink.next
      temp2 = newLink.next.next
      newLink.next = temp2
      temp1.next = temp2.next
      temp2.next = temp1
      newLink = temp1
    return newHead.next

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4])
  method = Solution()
  answer = method.swapPairs(head)
  print(answer)
from utils import ListNode
from utils import create_linked_list
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    tempo = dum = ListNode(0)
    while l1 and l2:
      if l1.val < l2.val:
        tempo.next = l1
        l1 = l1.next
      else:
        tempo.next = l2
        l2 = l2.next
      tempo = tempo.next
    tempo.next = l1 if l1 else l2
    return dum.next

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5, None])
  method = Solution()
  answer = method.reverseList(head)
  print(answer)
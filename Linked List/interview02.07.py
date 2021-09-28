from utils import ListNode
from utils import create_linked_list
class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    listSet = set()
    while headA:
      listSet.add(headA)
      headA  = headA.next
    while headB:
      if headB in listSet:
        return headB
      headB = headB.next
    return None

if __name__=="__main__":
  listA = create_linked_list([4, 1, 8, 4, 5])
  listB = create_linked_list([5, 0, 1, 8, 4, 5])
  method = Solution()
  answer = method.getIntersectionNode(listA, listB)
  print(answer)
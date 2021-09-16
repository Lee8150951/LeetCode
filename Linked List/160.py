from utils import ListNode
from utils import create_linked_list
class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # 哈希表
    hash = set()
    while headA:
      hash.add(headA)
      headA = headA.next
    while headB:
      if headB in hash:
        return headB
      headB = headB.next
    return


if __name__=="__main__":
  headA = create_linked_list([4, 1, 8, 4, 5])
  headB = create_linked_list([5, 0, 1, 8, 4, 5])
  method = Solution()
  answer = method.getIntersectionNode(headA, headB)
  print(answer)
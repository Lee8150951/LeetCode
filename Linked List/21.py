from utils import ListNode
from utils import create_linked_list
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 递归
    # if l1 is None:
    #   return l2
    # elif l2 is None:
    #   return l1
    # elif l1.val < l2.val:
    #   l1.next = self.mergeTwoLists(l1.next, l2)
    #   return l1
    # else:
    #   l2.next = self.mergeTwoLists(l2.next, l1)
    #   return l2

    # 迭代
    newLinkList = ListNode(-1)
    prev = newLinkList
    while l1 and l2:
      if l1.val < l2.val:
        prev.next = l1
        l1 = l1.next
      else:
        prev.next = l2
        l2 = l2.next
      prev = prev.next
    prev.next = l1 if l1 is not None else l2
    return newLinkList.next

if __name__=="__main__":
  l1 = create_linked_list([1, 2, 4])
  l2 = create_linked_list([1, 3, 4])
  method = Solution()
  answer = method.mergeTwoLists(l1, l2)
  print(answer)
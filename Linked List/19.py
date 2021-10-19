from utils import ListNode
from utils import create_linked_list
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # 两次遍历
    # point01 = head
    # length = 0
    # while point01:
    #   point01 = point01.next
    #   length += 1
    # if length == 1:
    #   return None
    # length = length - n
    # if length == 0:
    #   return head.next
    # point02 = head
    # for _ in range(length - 1):
    #   point02 = point02.next
    # point02.next = point02.next.next
    # return head

    # 单次遍历
    dummy = ListNode(0, head)
    first = head
    second = dummy
    for i in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next


if __name__=="__main__":
  head = create_linked_list([1, 2])
  n = 2
  method = Solution()
  answer = method.removeNthFromEnd(head, n)
  print(answer)
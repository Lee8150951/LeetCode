from utils import ListNode
from utils import create_linked_list
class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    # 设置 dummyNode 是这一类问题的一般做法
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    for _ in range(left - 1):
        pre = pre.next
        
    cur = pre.next
    for _ in range(right - left):
        next = cur.next
        cur.next = next.next
        next.next = pre.next
        pre.next = next
    return dummy_node.next


if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5])
  left = 2
  right = 4
  method = Solution()
  answer = method.reverseBetween(head, left, right)
  print(answer)
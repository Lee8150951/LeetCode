from utils import ListNode
from utils import create_linked_list

class Solution:
  def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    node, n = head, 0
    while node:
      node = node.next
      n += 1
    node = head
    for _ in range(n-k):
      node = node.next
    return node

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5])
  k = 2
  method = Solution()
  answer = method.getKthFromEnd(head, k)
  print(answer)
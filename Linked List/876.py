from utils import ListNode
from utils import create_linked_list
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    # 暴力解法
    # cur = head
    # length = 0
    # while cur:
    #   length += 1
    #   cur = cur.next
    # for _ in range(length // 2):
    #   head = head.next
    # return head

    # 快慢指针
    fast, slow = head, head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow
      

if __name__=="__main__":
  head = create_linked_list([1, 2, 3, 4, 5])
  method = Solution()
  answer = method.middleNode(head)
  print(answer)
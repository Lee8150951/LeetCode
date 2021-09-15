from utils import ListNode
from utils import create_linked_list
class Solution:
  # 单词循环哈希
  # def hasCycle(self, head: ListNode) -> bool:
  #   seen = set()
  #   while head:
  #     if head in seen:
  #       return True
  #     seen.add(head)
  #     head = head.next
  #   return False
  # 龟兔
  def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
      return False
    slow = head
    fast = head.next
    while slow != fast:
      if not fast or not fast.next:
        return False
      slow = slow.next
      fast = fast.next.next
    return True


if __name__=="__main__":
  head = create_linked_list([3, 2, 0, -4])
  method = Solution()
  answer = method.hasCycle(head)
  print(answer)
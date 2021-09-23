from utils import ListNode
from utils import create_linked_list
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    # 借助列表
    # cur = head
    # array = list()
    # while cur:
    #   array.append(cur.val)
    #   cur = cur.next
    # return array == array[::-1]

    # 找到前半部分链表的尾节点并反转后半部分链表
    first_half_end = self.end_of_first_half(head)
    second_half_start = self.reverse_list(first_half_end.next)
    # 判断是否回文
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
      if first_position.val != second_position.val:
        result = False
      first_position = first_position.next
      second_position = second_position.next
    # 还原链表并返回结果
    first_half_end.next = self.reverse_list(second_half_start)
    return result

  def end_of_first_half(self, head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
      fast = fast.next.next
      slow = slow.next
    return slow

  def reverse_list(self, head):
      previous = None
      current = head
      while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
      return previous

if __name__=="__main__":
  head = create_linked_list([1, 2, 1])
  method = Solution()
  answer = method.isPalindrome(head)
  print(answer)
from utils import ListNode
from utils import create_linked_list
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode(0)
    point_01 = l1
    point_02 = l2
    point_ans = ans
    carry = 0
    while point_01 or point_02:
      num_01 = point_01.val if point_01 else 0
      num_02 = point_02.val if point_02 else 0
      div = (num_01 + num_02 + point_ans.val) % 10
      carry = (num_01 + num_02 + point_ans.val) // 10
      if point_01: point_01 = point_01.next
      if point_02: point_02 = point_02.next
      point_ans.val = div
      if point_01 or point_02 or carry > 0:
        point_ans.next = ListNode(carry)
        point_ans = point_ans.next
    return ans.next
        

if __name__=="__main__":
  l1 = create_linked_list([2, 4, 3])
  l2 = create_linked_list([4, 5, 1, 9])
  method = Solution()
  answer = method.addTwoNumbers(l1, l2)
  print(answer)
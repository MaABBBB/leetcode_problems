
import pytest
from main import Solution, ListNode

class TestSolution:
    solution = Solution()

    def setup_nodes(self, node_vals: list[int]) -> ListNode:
        head = ListNode(val=node_vals[0])
        current = head
        for val in node_vals[1:]:
            current.next = ListNode(val=val)
            current = current.next
        return head
    
    def extract_val(self, node):
        while node:
            yield node.val
            node = node.next
    
    def test_1(self):
        l1 = self.setup_nodes([2,4,3])
        l2 = self.setup_nodes([5,6,4])
        ans = self.solution.addTwoNumbers(l1, l2)
        assert [val for val in self.extract_val(ans)] == [7, 0, 8]
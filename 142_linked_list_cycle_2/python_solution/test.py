from typing import Any

import pytest

from main import ListNode, Solution, Solution3

class TestSolution:
    @pytest.fixture
    def init_1(self):
        self.solution_1 = Solution()

    def _set_up_nodes(self, node_vals: list[Any], pos: int) -> ListNode:
        head = ListNode(x=node_vals[0])
        tail = head
        for val in node_vals[1:]:
            tail.next = ListNode(x=val)
            tail = tail.next

        temp = head
        for i in range(pos):
            temp = temp.next
        tail.next = temp
        return head

    def test_solution_1(self, init_1):
        head = self._set_up_nodes([3,2,0,-4], 1)
        assert self.solution_1.detectCycle(head).val == 2

    def test_solution_3(self):
        head = self._set_up_nodes([3,2,0,-4], 1)
        self.solution_3 = Solution3()
        assert self.solution_3.detectCycle(head).val == 2
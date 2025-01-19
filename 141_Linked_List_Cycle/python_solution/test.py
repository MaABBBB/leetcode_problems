from typing import Any

import pytest

from main import ListNode, Solution, Solution2, Solution_3

class TestSolution1:
    @pytest.fixture
    def init(self):
        self.solution = Solution()

    @pytest.fixture
    def init_2(self):
        self.solution_2 = Solution2()

    @pytest.fixture
    def init_3(self):
        self.solution_3 = Solution_3()

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

    def test_linked_list(self, init):
        head = self._set_up_nodes([3,2,0,-4], pos=1)
        assert self.solution.hasCycle(head) == True

    def test_linked_list_2(self, init_2):
        head = self._set_up_nodes([3,2,0,-4], pos=1)
        assert self.solution_2.hasCycle(head) == True

    def test_linked_list_3(self, init_3):
        head = self._set_up_nodes([3,2,0,-4], pos=1)
        assert self.solution_3.hasCycle(head) == True
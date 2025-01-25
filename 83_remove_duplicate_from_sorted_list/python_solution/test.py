import pytest

from main import Solution, ListNode

class TestSolution:

    @pytest.fixture
    def init_1(self):
        self.solution_1 = Solution()

    def setup_nodes(self, node_vals: list[int]) -> ListNode:
        head = ListNode(val=node_vals[0])
        current = head
        for val in node_vals[1:]:
            current.next = ListNode(val=val)
            current = current.next
        return head

    def test_1(self, init_1):
        head = self.setup_nodes([1,1,2,3,3])
        results = self.solution_1.deleteDuplicates(head=head)
        res = []
        while results:
            res.append(results.val)
            results = results.next
        assert res == [1,2,3]

    def test_2(self, init_1):
        head = self.setup_nodes([1,1,2,3,3])
        results = self.solution_1.deleteDuplicates2(head=head)
        res = []
        while results:
            res.append(results.val)
            results = results.next
        assert res == [1,2,3]

    def test_3(self, init_1):
        head = self.setup_nodes([1,1,2,3,3])
        results = self.solution_1.deleteDuplicates3(head=head)
        res = []
        while results:
            res.append(results.val)
            results = results.next
        assert res == [1,2,3]
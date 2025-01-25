import pytest
from main import ListNode, Solution

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
    
    def extract_val(self, node):
        while node:
            yield node.val
            node = node.next
    
    def test_1(self, init_1):
        head = self.setup_nodes([1,2,3,3,4,4,5])
        res = self.solution_1.deleteDuplicates(head)
        ans = []
        while res:
            ans.append(res.val)
            res = res.next

        assert ans == [1,2,5]

        head = self.setup_nodes([1,1,1,2,3])
        res = self.solution_1.deleteDuplicates(head=head)
        ans = [val for val in self.extract_val(res)]
        assert ans == [2,3]

    def test_2(self, init_1):
        head = self.setup_nodes([1,2,3,3,4,4,5])
        res = self.solution_1.deleteDuplicates_2(head)
        ans = []
        while res:
            ans.append(res.val)
            res = res.next

        assert ans == [1,2,5]

        head = self.setup_nodes([1,1,1,2,3])
        res = self.solution_1.deleteDuplicates_2(head=head)
        ans = [val for val in self.extract_val(res)]
        assert ans == [2,3]

    def test_3(self, init_1):
        head = self.setup_nodes([1,1,1,2,3])
        res = self.solution_1.deleteDuplicates_3(head=head)
        ans = [val for val in self.extract_val(res)]
        assert ans == [2,3]

        head = self.setup_nodes([1,2,3,3,4,4,5])
        res = self.solution_1.deleteDuplicates_3(head)
        ans = []
        while res:
            ans.append(res.val)
            res = res.next

        assert ans == [1,2,5]

        head = self.setup_nodes([1,1,1,2,3])
        res = self.solution_1.deleteDuplicates_3(head=head)
        ans = [val for val in self.extract_val(res)]
        assert ans == [2,3]

    def test_4(self, init_1):
        head = self.setup_nodes([1,1,1,2,3])
        res = self.solution_1.deleteDuplicates_4(head=head)
        ans = [val for val in self.extract_val(res)]
        assert ans == [2,3]

        head = self.setup_nodes([1,2,3,3,4,4,5])
        res = self.solution_1.deleteDuplicates_4(head)
        ans = []
        while res:
            ans.append(res.val)
            res = res.next

        assert ans == [1,2,5]

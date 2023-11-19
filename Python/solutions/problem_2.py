from .slnbase import Solution


class LLNode:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.nxt = nxt


class LList:
    def __init__(self, start: LLNode):
        self.start = start

    def __len__(self) -> int:
        cnt = 1
        node = self.start
        while True:
            cnt += 1
            if not node.nxt:
                break
            node = node.nxt

        return cnt

    def to_list(self) -> list:
        res = []
        node = self.start
        while True:
            res.append(node.val)
            if not node.nxt:
                break
            node = node.nxt

        return res

    def sum(self) -> int:
        val = 0
        m = 1
        node = self.start
        while True:
            val += m * node.val
            m *= 10
            if not node.nxt:
                break
            node = node.nxt

        return val


def get_int_ll(nums: list) -> LList:
    tail = LLNode(nums[-1])
    int_ll = LList(tail)
    for n in reversed(nums[:-1]):
        node = LLNode(n, tail)
        int_ll.start = node
        tail = node

    return int_ll


class Problem2(Solution):
    def __init__(self, s_name: str, ll1: LList, ll2: LList):
        super().__init__(s_name)
        self.ll1 = ll1
        self.ll2 = ll2

    def _solution(self):
        print("Sum = {}".format(self.ll1.sum() + self.ll2.sum()))

    def _alt_solution(self):
        pass

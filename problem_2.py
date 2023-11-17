import solution


class LLNode:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.nxt = nxt


class LList:
    def __init__(self, start: LLNode):
        self.start = start

    def __len__(self) -> int:
        cnt = 1
        ll_val = self.start
        while ll_val.nxt is not None:
            cnt += 1
            ll_val = ll_val.nxt

        return cnt


def get_int_ll(nums: list) -> LList:
    tail = LLNode(nums[-1])
    int_ll = LList(tail)
    for n in reversed(nums[:-1]):
        node = LLNode(n, tail)
        int_ll.start = node
        tail = node

    return int_ll


class Problem2(solution.Solution):
    def __init__(self, s_name: str, ll1: LList, ll2: LList):
        super().__init__(s_name)
        self.ll1 = ll1
        self.ll2 = ll2

    def _solution(self):
        l_lst = get_int_ll([i for i in range(0, 7)])
        print(len(l_lst))

    def _alt_solution(self):
        pass

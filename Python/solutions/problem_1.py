from .slnbase import Solution


class Problem1(Solution):
    def __init__(self, s_name: str, list_in: list, target: int):
        super().__init__(s_name)
        self.list_in = list_in
        self.target = target

    def _solution(self) -> tuple:
        t = self.target
        lst = self.list_in

        for i, el in enumerate(lst):
            if el > t:
                continue

            for j in range(i + 1, len(lst)):
                if lst[j] > t or i == j:
                    continue

                if (el + lst[j]) == t:
                    return i, j

    def _alt_solution(self):
        nums = {}
        for i, num in enumerate(self.list_in):
            nums[self.target - num] = i

        for i, num in enumerate(self.list_in):
            if nums.get(num):
                return i, nums[num]

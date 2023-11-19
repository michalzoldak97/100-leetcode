import pytest
import random

import Python.solutions as sln


class TestSolutions:
    def _set_problem_1(self):
        l_min, l_max = -1199999, 11
        lst = []
        for i in range(0, 9999):
            lst.append(random.randint(l_min, l_max))
        lst[5555] = 37
        lst[7777] = 54

        self.problem_1 = sln.Problem1("Two Sum", lst, 91)
        self.problem_1_res = (5555, 7777)

    def setup_method(self, method):
        self._set_problem_1()

    def test_problem_1(self):
        assert self.problem_1.run_solution() == self.problem_1_res

    def test_problem_1_alt(self):
        assert self.problem_1.run_solution(is_alternative=True) == self.problem_1_res

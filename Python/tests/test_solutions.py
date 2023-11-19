import pytest
import random

import Python.solutions as sln


class TestSolutions:
    def _set_problem_32(self):
        self.problem_32 = sln.Problem32("Longest p", '(()())()(())((()))()()(()(()))()()()()))(()()()')
        self.problem_32_res = 8

    def _set_problem_4(self):
        arr_m = [-53234, -654, -1, 0, 3, 542, 778, 9000, 12334, 654664]
        arr_n = [-13, -11, -2, -2, 54231, 90055, 123637, 275784]
        self.problem_4 = sln.Problem4('Sorted Median', arr_m, arr_n)
        self.problem_4_res = 272.5

    def _set_problem_3(self):
        self.problem_3 = sln.Problem3('Longest Substring', 'qwerhgudmlckhzorr620290*goknto gawtu0qpworweop,zvcjiw')
        self.problem_3_res = ('qwerhgudmlck', 12)

    def _set_problem_2(self):
        self.problem_2 = sln.Problem2('Add Two Numbers', sln.get_int_ll([5, 6, 6, 8, 9, 8, 9]),
                                      sln.get_int_ll([8, 8, 4, 7, 7, 8, 3]))
        self.problem_2_res = 13776153

    def _set_problem_1(self):
        l_min, l_max = -1199999, 11
        lst = []
        for i in range(0, 9999):
            lst.append(random.randint(l_min, l_max))
        lst[5555] = 37
        lst[7777] = 54

        self.problem_1 = sln.Problem1('Two Sum', lst, 91)
        self.problem_1_res = (5555, 7777)

    def setup_method(self, method):
        self._set_problem_1()
        self._set_problem_2()
        self._set_problem_3()
        self._set_problem_4()
        self._set_problem_32()

    def test_problem_1(self):
        assert self.problem_1.run_solution() == self.problem_1_res

    def test_problem_1_alt(self):
        assert self.problem_1.run_solution(is_alternative=True) == self.problem_1_res

    def test_problem_2(self):
        assert self.problem_2.run_solution() == self.problem_2_res

    def test_problem_3(self):
        assert self.problem_3.run_solution() == self.problem_3_res

    def test_problem_4(self):
        assert self.problem_4.run_solution() == self.problem_4_res

    def test_problem_4_alt(self):
        assert self.problem_4.run_solution(is_alternative=True) == self.problem_4_res

    def test_problem_32(self):
        assert self.problem_32.run_solution() == self.problem_32_res

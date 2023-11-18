import abc
import time
import tracemalloc


class Solution(abc.ABC):

    def __init__(self, s_name: str):
        self.s_name = s_name

    @abc.abstractmethod
    def _solution(self):
        """
            main method with the solution
        """

    @abc.abstractmethod
    def _alt_solution(self):
        """
            exemplary solution
        """

    def run_solution(self, is_alternative=False):
        t_start = time.clock()
        tracemalloc.start()

        if is_alternative:
            self._alt_solution()
        else:
            self._solution()

        print("Running {} took: {} and mem allocated was: {}".format(self.s_name,
                                                                     time.clock() - t_start,
                                                                     tracemalloc.get_traced_memory()))
        tracemalloc.stop()

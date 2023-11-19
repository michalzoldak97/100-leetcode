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
        t_start = time.process_time()
        tracemalloc.start()

        res = None

        if is_alternative:
            res = self._alt_solution()
        else:
            res = self._solution()

        print("\nRunning {} took: {} and mem allocated was: {}".format(self.s_name,
                                                                     time.process_time() - t_start,
                                                                     tracemalloc.get_traced_memory()))
        tracemalloc.stop()

        return res

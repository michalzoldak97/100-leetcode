import solution
import math


class Problem4(solution.Solution):
    def __init__(self, s_name: str, arr_m: list, arr_n: list):
        super().__init__(s_name)
        self.arr_m = arr_m
        self.arr_n = arr_n

    def _solution(self):
        mn_len = len(self.arr_m) + len(self.arr_n)
        arr_mn = [0 for _ in range(mn_len)]

        arr_lower, arr_higher = [], []
        if self.arr_m[0] < self.arr_n[0]:
            arr_lower, arr_higher = self.arr_m, self.arr_n
        else:
            arr_lower, arr_higher = self.arr_n, self.arr_m

        l_idx, h_idx = 0, 0
        for i, _ in enumerate(arr_mn):
            if l_idx == len(arr_lower):
                arr_mn[i] = arr_higher[h_idx]
                h_idx += 1
                continue

            if h_idx == len(arr_higher):
                arr_mn[i] = arr_lower[h_idx]
                l_idx += 1
                continue

            if arr_lower[l_idx] < arr_higher[h_idx]:
                arr_mn[i] = arr_lower[l_idx]
                l_idx += 1
            else:
                arr_mn[i] = arr_higher[h_idx]
                h_idx += 1

        if mn_len % 2 == 0:
            h = int(mn_len / 2)
            print("median is {}".format((arr_mn[h - 1] + arr_mn[h]) / 2.))
        else:
            print("median is {}".format(arr_mn[math.floor(mn_len / 2.)]))

    def _find_median(self, nums: list) -> float:
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        else:
            return nums[len(nums) // 2]

    def _alt_solution(self):
        merge = []
        i, j = 0, 0
        while i < len(self.arr_m) or j < len(self.arr_n):
            if i == len(self.arr_m):
                merge.append(self.arr_n[j])
                j += 1
            elif j == len(self.arr_n):
                merge.append(self.arr_m[i])
                i += 1
            elif self.arr_m[i] < self.arr_n[j]:
                merge.append(self.arr_m[i])
                i += 1
            else:
                merge.append(self.arr_n[j])
                j += 1

        print("median is {}".format(self._find_median(merge)))

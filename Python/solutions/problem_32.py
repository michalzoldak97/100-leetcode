from .slnbase import Solution


class Problem32(Solution):
    def __init__(self, s_name: str, phr: str):
        super().__init__(s_name)
        self.phr = phr

    def _solution(self) -> int:
        max_cnt = 0
        cnt = 0
        should_skip = False
        for i, rc in enumerate(self.phr[1:]):
            if should_skip:
                should_skip = False
                continue

            lc = self.phr[i]

            if lc == "(" and rc == ")":
                cnt += 2
                if cnt > max_cnt:
                    max_cnt = cnt
                should_skip = True
                continue

            cnt = 0

        return max_cnt

    def _alt_solution(self):
        pass

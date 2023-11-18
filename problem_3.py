import solution


class Problem3(solution.Solution):
    def __init__(self, s_name: str, s_in: str):
        super().__init__(s_name)
        self.s_in = s_in

    def _solution(self):
        max_cnt = 1
        max_str = self.s_in[0]
        unique_str = self.s_in[0]

        for c in self.s_in[1:]:
            if c not in unique_str:
                unique_str += c
                continue

            curr_len = len(unique_str)
            if curr_len > max_cnt:
                max_cnt = curr_len
                max_str = unique_str

            unique_str = c

        print(max_str, len(max_str))

    def _alt_solution(self):
        s = list(self.s_in)
        start = 0
        length = 0
        max_length = 0
        tmp_str = s[0]
        max_str = s[0]
        for idx, l in enumerate(s):
            if l in s[start:idx]:
                start = s.index(l, start, idx) + 1
                length = len(s[start:idx]) + 1
                tmp_str = l
            else:
                length += 1
                tmp_str += l
                if length > max_length:
                    max_length = length
                    max_str = tmp_str
        print(max_str, max_length)

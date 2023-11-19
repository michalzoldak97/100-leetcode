import random
import string

import Python.solutions as sln


def run_32():
    s = "(()"
    p = sln.Problem32("Longest p", s)
    p.run_solution()


def run_4():
    random.seed(367687759840784)
    arr_m = [random.randint(-999999, 999999) for _ in range(random.randint(10000, 99999))]
    arr_n = [random.randint(-999999, 999999) for _ in range(random.randint(10000, 99999))]
    p = sln.Problem4("Sorted Median", arr_m, arr_n)
    p.run_solution(is_alternative=False)


def run_3():
    random.seed(6567368)
    phrase = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100000))
    p = sln.Problem3("Longest Substring", phrase)
    p.run_solution(is_alternative=False)


def run_2():
    l1 = [random.randint(1, 9) for _ in range(3)]
    l2 = [random.randint(1, 9) for _ in range(3)]
    ll1, ll2 = sln.get_int_ll(l1), sln.get_int_ll(l2)
    print("{}\n{}".format(ll1.to_list(), ll2.to_list()))
    p = sln.Problem2("Add Two Numbers", ll1, ll2)
    p.run_solution()


def run_1():
    l_min, l_max = -1199999, 11
    lst = []
    for i in range(0, 9999):
        lst.append(random.randint(l_min, l_max))
    lst[5555] = 37
    lst[7777] = 54

    p = sln.Problem1("Two Sum", lst, 91)
    p.run_solution(is_alternative=True)


def main():
    run_32()


if __name__ == "__main__":
    main()
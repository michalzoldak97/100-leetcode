import random
import problem_1
import problem_2


def run_2():
    l1 = [random.randint(1, 9) for _ in range(3)]
    l2 = [random.randint(1, 9) for _ in range(3)]
    ll1, ll2 = problem_2.get_int_ll(l1), problem_2.get_int_ll(l2)
    print("{}\n{}".format(ll1.to_list(), ll2.to_list()))
    p = problem_2.Problem2("Add Two Numbers", ll1, ll2)
    p.run_solution()


def run_1():
    l_min, l_max = -1199999, 11
    lst = []
    for i in range(0, 9999):
        lst.append(random.randint(l_min, l_max))
    lst[5555] = 37
    lst[7777] = 54

    p = problem_1.Problem1("Two Sum", [1,5,3,4,6,9,3,37,7,3,1,-7,0,4,2,54,6,7,7,7,3,1,8,7,5], 91)
    p.run_solution(is_alternative=True)


def main():
    run_2()


if __name__ == "__main__":
    main()

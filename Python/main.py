import Python.solutions as sln


def run_32():
    s = "(()())()(())((()))()()(()(()))()()()()))(()()()"
    p = sln.Problem32("Longest p", s)
    print(p.run_solution())


def main():
    run_32()


if __name__ == "__main__":
    main()

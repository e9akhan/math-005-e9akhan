"""
    Module name :- solver
    Method(s) :- solver(p, q)
"""


def solver(p, q):
    """
    Find the number which is divisible by each number
    over the range.

    Args:
        p(int) :- Starting point of the range
        q(int) :- Ending point of the range.

    Return:
        Smallest number which is divisible by each number
        over the range.
    """
    number = 0

    if p > q:
        temp, p = p, q
        q = temp

    while True:
        number += q
        for i in range(p, q + 1):
            if number % i != 0:
                break
        else:
            return number


if __name__ == "__main__":
    print(solver(1, 20))

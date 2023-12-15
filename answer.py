"""
    Module name :- answer.py
    Method(s) :- answer()
"""

from solver import solver


def answer():
    """
    Find the smallest positive number which is divisible by
    each number from 1-10
    """
    return solver(1, 10)


if __name__ == "__main__":
    print(answer())

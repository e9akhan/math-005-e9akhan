"""
    Module name :- solver
    Method(s) :- solver(p, q)
"""

def gcd(x, y):
    """
        Find the GCD of x and y.

        Args:-
            x(int) :- First integer number
            y(int) :- Second integer number

        Return
            GCD of two numbers
    """
    return y and gcd(y, x%y) or x

def lcm(x, y):
    """
        Find the LCM of x and y.

        Args:-
            x(int) :- First integer number
            y(int) :- Second integer number

        Return
            LCM of two numbers
    """
    return x*y/gcd(x, y)

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
    number = 1

    if p > q:
        return -1

    for i in range(p, q):
        number = lcm(number, i)

    return int(number)


if __name__ == "__main__":
    print(f'solver(1, 10) = {solver(1, 10)}')

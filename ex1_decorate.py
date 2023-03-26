"""
Writer: Ranel Ben Simman Tov
"""

from functools import wraps


class ArgumentTypeError(Exception):
    pass


def type_check(correct_type):
    """
    check if the argument passed to the function is of the correct type
    :param correct_type: the correct type of the argument
    :return: the function if the argument is of the correct type
    """
    def check_decorator(func):
        @wraps(func)
        def check_func(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            raise ArgumentTypeError(f'Argument passed is not of type {correct_type}')
        return check_func
    return check_decorator


@type_check(int)
def times2(num):
    return num * 2


if __name__ == '__main__':
    try:
        print(times2('7'))
    except ArgumentTypeError as e:
        print(e)
